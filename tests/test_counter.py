from lib.counter import *
def test_returns_zero():
    counter = Counter()
    assert counter.count == 0

def test_returns_six():
    counter = Counter()
    counter.add(6)
    assert counter.count == 6

def test_report():
    counter = Counter()
    counter.add(6)
    assert counter.report() == "Counted to 6 so far."
