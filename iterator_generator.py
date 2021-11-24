from _collections_abc import Iterable


class Iterator:
    def __init__(self, data: list) -> None:                 # class constructor
        self.list = data                                    # assigning an itter object
        self.counter = -1                                   # counter of iterations
        self.len = len(data)                                # the length of the list, for optimization

    def __iter__(self) -> Iterable:                         # iterator method
        return self

    def __next__(self) -> any:                              # next step of itter
        while self.counter < self.len - 1:                  # control of the number of iterations
            self.counter += 1                               # counter of iterations
            return self.list[self.counter]                  # return next index of list
        raise StopIteration


def gen(data):
    for i in data:
        yield i


a = [1, 2, 3, 4, 5, 6, 7, 8]
a_iter = Iterator(data=a)
print(type(a_iter))
for line in Iterator(data=a):
    print(line, end=' ')

print()
a_gen = gen(data=a)
print(type(a_gen))
for line in a_gen:
    print(line, end=' ')
