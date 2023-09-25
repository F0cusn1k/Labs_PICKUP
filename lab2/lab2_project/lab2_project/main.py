import numpy as np

from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square

def main():
    rect = Rectangle(17, 17, "Blue")
    print(rect.repr())
    circ = Circle(17, "Green")
    print(circ.repr())
    sq = Square(17, "Red")
    print(sq.repr())
    a1D = np.array([1, 2, 3, 4])
    print(a1D)


if __name__ == "__main__":
    main()