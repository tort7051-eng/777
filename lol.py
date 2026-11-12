class MyIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return (x for x in range(self.start, self.end + 1))


numbers = MyIterable(1, 5)

for number in numbers:
    print(number)
