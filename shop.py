def add(a, b):
    return a + b


def calculate_total(prices):
    return sum(prices)


def apply_discount(total, percentage):
    if percentage < 0 or percentage > 100:
        raise ValueError("Invalid discount percentage")

    return total * (1 - percentage / 100)


def is_valid_quantity(quantity):
    return (
        isinstance(quantity, int)
        and not isinstance(quantity, bool)
        and quantity > 0
    )