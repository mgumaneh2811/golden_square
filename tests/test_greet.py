from lib.greet import*
def test_greet():
    result = greet("Diana")
    assert result == "Hello, Diana!"
