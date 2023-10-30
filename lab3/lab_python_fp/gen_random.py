from random import randint

def gen_random(num_count, begin, end):
    res = []
    for i in range(num_count):
        res.append(randint(begin, end))
    return res

def main():
    print(*gen_random(5, 1, 3), sep=', ')

if __name__ == '__main__':
    main()
