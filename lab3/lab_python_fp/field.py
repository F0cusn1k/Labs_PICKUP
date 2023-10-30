def field(items, *args):
    if len(args) == 1:
        res = []
        for i in items:
            if i[args[0]]:
                res.append(i[args[0]])
        return res

    res = []
    for i in items:
        temp = {}
        for a in args:
            if i[a]:
                temp[a] = i[a]
        if temp:
            res.append(temp)
    return tuple(res)


def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    print(*field(goods, 'title'), sep=', ')
    print(*field(goods, 'title', 'price'), sep=', ')


if __name__ == '__main__':
    main()
