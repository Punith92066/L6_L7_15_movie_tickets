
import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# Ticket price tests

def test_regular_morning():
    assert ticket_price("regular", 25, 10, False) == 100


def test_premium_evening_weekend():
    assert ticket_price("premium", 25, 19, True) == 320


def test_recliner_afternoon():
    assert ticket_price("recliner", 25, 15, False) == 400


def test_toddler_free_ticket():
    assert ticket_price("regular", 2, 15, False) == 0


def test_child_discount():
    assert ticket_price("regular", 10, 15, False) == 75


def test_senior_discount():
    assert ticket_price("premium", 60, 15, False) == 125


def test_invalid_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("vip", 25, 15, False)


def test_invalid_show_time_negative():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, -1, False)


def test_invalid_show_time_above_23():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 24, False)


# Group discount tests

def test_one_ticket():
    assert group_discount(1, False) == 0


def test_five_tickets():
    assert group_discount(5, False) == 10


def test_ten_tickets():
    assert group_discount(10, False) == 15


def test_student_group_discount():
    assert group_discount(5, True) == 15


def test_invalid_group():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


# Snack combo tests

def test_small_snack():
    assert snack_combo("small", False) == 120


def test_medium_snack():
    assert snack_combo("medium", False) == 180


def test_large_snack():
    assert snack_combo("large", False) == 250


def test_small_snack_coupon():
    assert snack_combo("small", True) == 70
