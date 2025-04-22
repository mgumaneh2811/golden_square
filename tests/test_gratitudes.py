from lib.gratitudes import *
def test_gratitude_returns_empty_list():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []

def test_word_is_added():
    gratitudes = Gratitudes()
    gratitudes.add("life")
    assert gratitudes.gratitudes == ["life"]

def test_a_formatted_version():
    gratitudes = Gratitudes()
    gratitudes.add("life")
    gratitudes.add("family")
    assert gratitudes.format() == "Be grateful for: life, family"
