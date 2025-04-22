# if given an empty string returns empty string
from lib.make_snippet import *
def test_given_empty_string_returns_empty_string():
    result = make_snippet("")
    assert result == ""

# if given four words we return four words
def test_given_four_words_returns_four_words():
    result = make_snippet("one two three four")
    assert result == "one two three four"

# if given five words we return five words
def test_given_five_words_returns_five_words():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

# if given 6 words we return first 5 words + '...'
def test_given_6_words_returns():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."