import pytest
from numb3rs import validate

def test_ip():

    assert validate('127.0.0.1') == True
    assert validate('0.0.0.0') == True
    assert validate('255.255.255.255') == True
    assert validate('500.0.0.1') == False
    assert validate('1.2.3.1000') == False
    assert validate('cat') == False

def test_first_byte():

    assert validate('255.500.0.0') == False
