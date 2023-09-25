import sys
import math

class Solver:
    def __init__(self, mass):
        while (1):
            for i in range(len(mass)):
                if mass[i] == None:
                    print("Введите коэффициент номер {}: ".format(i+1), end = '')
                    try:
                        mass[i] = float(input())
                    except:
                        print("Ошибка")
            if mass[0] == 0:
                mass[0] = None
            if(mass[0]!=None and mass[1]!=None and mass[2]!=None):
                break
        self.a = mass[0]
        self.b = mass[1]
        self.c = mass[2]
        self.roots = list()
        self.D = self.b*self.b - 4*self.a*self.c

    def solve(self):
        if self.D < 0:
            return

        sqD = math.sqrt(self.D)
        root1 = (-self.b + sqD) / (2.0*self.a)
        root2 = (-self.b - sqD) / (2.0*self.a)
        res = list()
        if (root1 >= 0):
            self.roots.append(math.sqrt(root1))
            self.roots.append(-math.sqrt(root1))
        if (root2 >= 0):
            self.roots.append(math.sqrt(root2))
            self.roots.append(-math.sqrt(root2))
        self.roots = list(set(self.roots))

    def show(self):
        len_roots = len(self.roots)
        if len_roots == 0:
            print('Нет корней')
        else:
            print('Количество корней уравнения {}. Корни: '.format(len_roots), end = '')
            for i in self.roots:
                print(i, end = '  ')
        
        


def main():
    sys2 = [0 for i in range(3)]
    for i in [1, 2, 3]:
        try:
            sys2[i-1] = sys.argv[i]
        except:
            sys2[i-1] = None

    equation = Solver(sys2)
    equation.solve()
    equation.show()


if __name__ == "__main__":
    main()
