from shop import add, calculate_total


def test_addition():
    assert add(1, 1) == 2


def test_calculate_total():
    assert calculate_total([10, 20, 30]) == 60


def test_empty_total():
    assert calculate_total([]) == 0


def test_string_uppercase():
    assert "hello".upper() == "HELLO"


def test_list_length():
    fruits = ["apple", "banana", "cherry"]
    assert len(fruits) == 3