from lib.string_builder import*
def test_string_builder_is_an_emppty_string():
    stringbuilder = StringBuilder()
    assert stringbuilder.output() == ""

def test_add_method():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    assert stringbuilder.output() == "hello"

def test_len_method():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    assert stringbuilder.size() == 5

def test_behaviour():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    stringbuilder.add("world")
    assert stringbuilder.output() == "helloworld"
    assert stringbuilder.size()== 10