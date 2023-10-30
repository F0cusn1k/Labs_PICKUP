def print_result(func):
    def f(*args, **kwargs):
        print(func.__name__)
        res = func(*args, **kwargs)
        if isinstance(res, list):
            for i in res:
                print(i)
            return res
        elif isinstance(res, dict):
            for key, value in res.items():
                print('{} = {}'.format(key, value))
            return res
        else:
            print(res)
            return res

    return f


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


def main():
    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    main()
