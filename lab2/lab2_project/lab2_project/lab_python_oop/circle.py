from lab_python_oop.color import Color
from lab_python_oop.geom_figure import Figure
from abc import ABC, abstractmethod
import math

class Circle(Figure):
    def __init__(self, radius_, color_):
        self.radius = radius_
        self.my_color = Color(color_)
        self.name = "Круг"
    def area(self):
        return math.pi*self.radius*self.radius
    def return_name(self):
        return self.name
    def repr(self):
        return "Тип фигуры - {}, Радиус - {}, Цвет - {}, Площадь - {}".format(self.return_name(),
                                                                              self.radius,
                                                                              self.my_color.color,
                                                                              self.area())
