import pytest
from working import convert

def test_both():

    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'
    assert convert('12 PM to 12 AM') == '12:00 to 00:00'

def test_reverse():

    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'

def test_wrong_time():

    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60')

    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')

    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')

    with pytest.raises(ValueError):
        convert('9AM to 5PM')

    with pytest.raises(ValueError):
        convert('9:62 AM to 14 PM')


