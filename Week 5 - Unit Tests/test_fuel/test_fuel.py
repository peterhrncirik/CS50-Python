from fuel import convert, gauge
import pytest


def test_cnvrt():

    assert convert("1/1") == 100
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("1/100") == 1


    with pytest.raises(ZeroDivisionError):
        convert("3/0")

    with pytest.raises(ValueError):
        convert("a/b")


def test_g():

    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
