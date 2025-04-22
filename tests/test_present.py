from lib.present import*
import pytest
def test_present():
    present = Present()
    assert present.contents == None

def test_wrap():
    present = Present()
    present.contents = "something"
    with pytest.raises(Exception) as err:
        present.wrap("")
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrap():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."

