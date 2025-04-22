from lib.check_codeword import*
def test_check_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."