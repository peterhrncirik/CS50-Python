class Jar:

    def __init__(self, capacity=12, cookies=0):

        if capacity <= 0:
            raise ValueError('You will need a bigger jar')

        self.capacity = capacity
        self.cookies = cookies

    def __str__(self):
        return self.cookies * '🍪'

    def deposit(self, n):

        if (self.cookies + n) > self.capacity:
            raise ValueError('Not enough space')

        self.cookies += n

    def withdraw(self, n):

        if n > self.cookies:
            raise ValueError('You don\'t have that many cookies')

        self.cookies -= n

    @property
    def total(self):
        return self.capacity

    @property
    def size(self):
        return self.cookies

