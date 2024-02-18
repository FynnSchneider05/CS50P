class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return ("🍪" * self.size)


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if type(capacity) == int and capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError()


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size <= self.capacity:
            self._size = size



    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError("Not enough capacity in the jar")


    def withdraw(self, n):
        if self.size - n >= 0:
            self.size -= n
        else:
            raise ValueError("Not enough cookies in the jar")


def main():
    try:
        jar = Jar()
    except ValueError:
        raise ValueError("capacity must be an non-negative-integer")


if __name__ == "__main__":
    main()
