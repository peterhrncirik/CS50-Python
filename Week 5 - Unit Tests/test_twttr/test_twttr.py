from twttr import shorten

def test_lower():

    assert shorten('twitter') == 'twttr'

def test_capital():

    assert shorten('TWITTER') == 'TWTTR'

def test_empty():

    assert shorten('') == ''

def test_punctuation():

    assert shorten('1TWITTER!') == '1TWTTR!'
