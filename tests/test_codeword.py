from lib.check_codeword import *
def test_if_codeword_is_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_first_and_last_charachter():
    result = check_codeword("helle")
    assert result == "Close, but nope."

def test_wrong_word():
    result = check_codeword("mouse")
    assert result == "WRONG!"