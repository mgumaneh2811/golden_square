from lib.greet import *
def test_greet_returns_hello_name():
    greeting = greet("Isa")
    assert greeting == "Hello, Isa!"