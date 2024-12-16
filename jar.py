class Jar:
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.size = 0

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not (type(capacity) is int and  capacity > 0):
            raise ValueError("wrong capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not (type(size) is int and size >= 0 and size <= self.capacity):
            raise ValueError("size problems")
        self._size = size

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Cannot deposit cookies beyond the jar's capacity.")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
            raise ValueError("Cannot withdraw more cookies than are currently in the jar.")
        self._size -= n







