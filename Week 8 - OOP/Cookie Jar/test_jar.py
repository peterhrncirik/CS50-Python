import pytest
from jar import Jar

def test_default():

    # initiate
    jar = Jar()

    assert str(jar) == ""

def test_deposit():

    # initiate
    jar = Jar()

    jar.deposit(2)
    assert str(jar) == "🍪🍪"

    # change capacity to lower and try to deposit more
    jar1 = Jar(4)

    with pytest.raises(ValueError):
        jar1.deposit(10)

def test_withdraw():

    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

    # withdraw more than available
    jar1 = Jar()
    jar1.deposit(10)

    with pytest.raises(ValueError):
        jar1.withdraw(11)

def test_total():

    jar = Jar(10)
    assert jar.total == 10

def test_size():

    jar = Jar(10)

    # capacity is 10 but actual cookies are 0
    assert jar.size == 0

    # add cookies
    jar.deposit(5)
    assert jar.size == 5




