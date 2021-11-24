class Iterator:
    def __init__(self, data: list):
        self.list = data
        self.counter = -1
        self.len = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < self.len - 1:
            self.counter += 1
            return self.list[self.counter]
        raise StopIteration


def gen(data):
    for i in data:
        yield i


a = [1, 2, 3, 4, 5, 6, 7, 8]
a_iter = Iterator(data=a)
a_gen = gen(data=a)
for line in a_gen:
    print(line, end=' ')

print()
for line in Iterator(data=a):
    print(line, end=' ')
