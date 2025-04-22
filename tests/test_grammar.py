from lib.grammar import *
import pytest

def test_a_string_exists():
    assert grammar_text("") == False

def test_first_letter_capital_and_last_letter_is_punctuation():
    assert grammar_text("Birmingham.") == True

def test_first_letter_capital_and_last_letter_is_not_punctuation():
    assert grammar_text("Birmingham") == False

def test_first_letter_not_capital_and_last_letter_punctuated():
    assert grammar_text("birmingham.") == False

def test_with_incorrect_puntuation():
    assert grammar_text("Birmingham,") == False
