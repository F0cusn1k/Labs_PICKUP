from gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.res = set()
        self.mass = items
        self.i = 0

        if 'ignore_case' not in kwargs:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        if self.ignore_case:
            for i, el in enumerate(self.mass):
                if isinstance(el, str):
                    self.mass[i] = el.lower()

        while True:
            if self.i >= len(self.mass):
                raise StopIteration
            else:
                t = self.mass[self.i]
                self.i += 1
                if t not in self.res:
                    self.res.add(t)
                    return t

    def __iter__(self):
        return self


def main():
    print('ЗАДАНИЕ 1')
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for item in Unique(data):
        print(item)

    print('ЗАДАНИЕ 2')
    data = gen_random(10, 1, 3)
    for item in Unique(data):
        print(item)

    print('ЗАДАНИЕ 3')
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for item in Unique(data):
        print(item)

    print('ЗАДАНИЕ 4')
    for item in Unique(data, ignore_case=True):
        print(item)


if __name__ == '__main__':
    main()
