from abc import ABC, abstractmethod

class Color(ABC):

    def __init__(self, color_):
        self.__color = color_

    def get_color(self):
        return self.__color

    def set_color(self, color_):
        self.__color = color_

    color = property(get_color, set_color)
