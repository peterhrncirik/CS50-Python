import pytest
from um import count

def test_words():

    assert count('Um, thats yummy') == 1
    assert count('That new album is awesome') != 1

def test_numbers():

    assert count('123456789') == 0

def test_beginning():

    assert count('Ummm okay') == 0

def test_ending():

    assert count('That was yumm ummm') == 0
