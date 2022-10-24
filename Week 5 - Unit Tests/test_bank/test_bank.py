from bank import value

def test_hello():

    assert value('Hello') == 0
    assert value('hello') == 0

def test_first():

    assert value('how are you') == 20

def test_other():

    assert value('What is up?') == 100
