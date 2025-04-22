from lib.counter import*
def test_counter():
    counter = Counter ()
    counter.add(2)
    result = counter.report()
    assert result == "Counted to 2 so far."