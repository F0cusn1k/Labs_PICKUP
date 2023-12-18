import sys
import math

#Ф-я вычисления коэффициентов
def get_coef(index, prompt):
    if (index < len(sys.argv)):
        try:
            return float(sys.argv[index])
        except:
            return get_coef(404, prompt)
    
    print(prompt, end = ' ')
    try:
        return float(input())
    except:
        return get_coef(index, prompt)


# Вычисление корней
def get_roots(a, b, c):
    D = b*b - 4*a*c
    if D < 0:
        return list()

    sqD = math.sqrt(D)
    root1 = (-b + sqD) / (2.0*a)
    root2 = (-b - sqD) / (2.0*a)
    res = list()
    if (root1 >= 0):
        res.append(math.sqrt(root1))
        res.append(-math.sqrt(root1))
    if (root2 >= 0):
        res.append(math.sqrt(root2))
        res.append(-math.sqrt(root2))
    return list(set(res))


def main():
    a = 0
    while(a==0):
        a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a,b,c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    else:
        print('Количество корней уравнения {}. Корни: '.format(len_roots), end = '')
        for i in roots:
            print(i, end = '  ')
    

if __name__ == "__main__":
    main()
