from lab_python_oop.color import Color
from lab_python_oop.geom_figure import Figure
from lab_python_oop.rectangle import Rectangle
from abc import ABC, abstractmethod

class Square(Rectangle):
    def __init__(self, L_, color_):
        self.L = L_
        self.my_color = Color(color_)
        self.name = "Квадрат"
    def area(self):
        return self.L*self.L
    def return_name(self):
        return self.name
    def repr(self):
        return "Тип фигуры - {}, Длина стороны - {}, Цвет - {}, Площадь - {}".format(self.return_name(),
                                                                                     self.L,
                                                                                     self.my_color.color,
                                                                                     self.area())
