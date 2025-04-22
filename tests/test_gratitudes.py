from lib.gratitudes import*

def test_gratitudes():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []

def test_add_function():
    gratitudes = Gratitudes()
    gratitudes.add("life")
    assert gratitudes.gratitudes == ["life"]

def test_format_function():
    gratitudes = Gratitudes()
    gratitudes.add("life")
    gratitudes.add("health")
    assert gratitudes.format() == "Be grateful for: life, health"
