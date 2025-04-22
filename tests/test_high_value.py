from lib.high_value import*


def test_highest_value():
    value = HighValue(10, 9)
    assert value.get_highest() == "First value is higher"

def test_lower_value():
    value = HighValue(0, 24)
    assert value.get_highest() == "Second value is higher"

def test_if_equal():
    value = HighValue(24, 24)
    assert value.get_highest() == "Values are equal"

def test_if_added_first_value():
    something = HighValue(4, 24)
    something.add(5, "first")
    assert something.value_first == 9

def test_if_added_second_value():
    something = HighValue(4, 24)
    something.add(6, "another choice")
    assert something.value_second == 30
