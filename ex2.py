class PowerGenerator:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return self.a**self.i
        else:
            raise StopIteration


powers = PowerGenerator(2, 8)

for value in powers:
    print(value)
