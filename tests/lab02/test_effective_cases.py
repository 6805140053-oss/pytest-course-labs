import pytest

from shop import (
    calculate_total,
    apply_discount,
    is_valid_quantity
)


def test_calculate_total_with_multiple_prices():
    # Arrange
    prices = [100, 200, 300]

    # Act
    result = calculate_total(prices)

    # Assert
    assert result == 600


def test_calculate_total_with_empty_list():
    prices = []

    result = calculate_total(prices)

    assert result == 0


def test_discount_of_10_percent():
    total = 100

    result = apply_discount(total, 10)

    assert result == 90


def test_discount_of_100_percent():
    total = 100

    result = apply_discount(total, 100)

    assert result == 0


def test_negative_discount_is_rejected():
    with pytest.raises(ValueError):
        apply_discount(100, -10)


def test_discount_over_100_is_rejected():
    with pytest.raises(ValueError):
        apply_discount(100, 110)


def test_valid_quantity():
    assert is_valid_quantity(5) is True


def test_zero_quantity_is_invalid():
    assert is_valid_quantity(0) is False