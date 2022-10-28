import pytest
from seasons import convert, check_input

def test_inputs():

    # check incorrect date
    with pytest.raises(ValueError):
        check_input('2000-13-32')
