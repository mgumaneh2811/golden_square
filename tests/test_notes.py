from lib.notes import *

def test_empty_is_returned():
    result = find_TODO("")
    assert result == False

def test_string_is_returned():
    result = find_TODO("buy milk")
    assert result == False

def test_for_TODO():
    result = find_TODO("TODO buy milk")
    assert result == True