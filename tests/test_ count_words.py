from lib.count_words import *
# test what happens with an empty string
def test_empty_string_returns_zero():
    result = count_words("")
    assert result == 0

# test what happens with one word
def test_one_word():
    result = count_words("one")
    assert result == 1

# test what happens with two words
def test_two_words():
    result = count_words("TWO WORDS")
    assert result ==  2

# test what happens with three words
def test_three_words():
    result = count_words("TWO WORDS and")
    assert result ==  3