
import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# Ticket price: seat validation

def test_branch_invalid_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("invalid", 25, 15, False)


# Ticket price: show time validation

def test_branch_invalid_time_below_zero():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, -1, False)


def test_branch_invalid_time_above_23():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 24, False)


# Ticket price: morning, afternoon, evening

def test_branch_morning():
    assert ticket_price("regular", 25, 10, False) == 100


def test_branch_afternoon():
    assert ticket_price("regular", 25, 15, False) == 150


def test_branch_evening():
    assert ticket_price("regular", 25, 19, False) == 180


# Ticket price: weekend

def test_branch_weekday():
    assert ticket_price("regular", 25, 15, False) == 150


def test_branch_weekend():
    assert ticket_price("regular", 25, 15, True) == 190


# Ticket price: age conditions

def test_branch_age_below_three():
    assert ticket_price("regular", 2, 15, False) == 0


def test_branch_age_three():
    assert ticket_price("regular", 3, 15, False) == 75


def test_branch_age_twelve():
    assert ticket_price("regular", 12, 15, False) == 75


def test_branch_age_thirteen():
    assert ticket_price("regular", 13, 15, False) == 150


def test_branch_age_fifty_nine():
    assert ticket_price("regular", 59, 15, False) == 150


def test_branch_age_sixty():
    assert ticket_price("regular", 60, 15, False) == 75


# Group discount: ticket count

def test_branch_no_tickets():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_branch_below_five_tickets():
    assert group_discount(2, False) == 0


def test_branch_exactly_five_tickets():
    assert group_discount(5, False) == 10


def test_branch_exactly_ten_tickets():
    assert group_discount(10, False) == 15


# Group discount: student conditions

def test_branch_student_with_discount():
    assert group_discount(5, True) == 15


def test_branch_student_without_discount():
    assert group_discount(2, True) == 0


def test_branch_non_student_with_discount():
    assert group_discount(5, False) == 10


# Snack combo: size

def test_branch_small_snack():
    assert snack_combo("small", False) == 120


def test_branch_medium_snack():
    assert snack_combo("medium", False) == 180


def test_branch_large_snack():
    assert snack_combo("large", False) == 250


# Snack combo: coupon

def test_branch_coupon_applied():
    assert snack_combo("small", True) == 70


def test_branch_no_coupon():
    assert snack_combo("small", False) == 120
