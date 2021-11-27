import math


class Square:
    """
    Класс фигуры квадрат. Геттер и сеттер на длину стороны.
    Arg:
        length - длина стороны квадрата
    Arguments:
        __length - инкапсулированная длина стороны квадрата
    """

    def __init__(self, length: float) -> None:
        self.length = length

    @property
    def length(self) -> float:
        """Геттер длины стороны квадрата"""
        return self.__length

    @length.setter
    def length(self, new_length) -> None:
        """Сеттер длины стороны квадрата"""
        self.__length = new_length

    def square(self) -> float:
        """Возвращает площадь квадрата"""
        return self.length ** 2

    def perimeter(self) -> float:
        """Возвращает периметр квадрата"""
        return self.length * 4


class Cube(Square):
    """
    Класс описывающий фигуру куб
        Arg:
        length - длина ребра куба
    Arguments:
        faces_list - список площадей граней куба
    """

    def __init__(self, length: float) -> None:
        super().__init__(length=length)
        self.faces_list = [self.square() for _ in range(6)]

    def __str__(self):
        """Представление экземпляра, возвращает строку с описанием"""
        return 'Куб с длиной ребра: {}\nсписок площадей граней: {}'.format(
            self.length,
            self.faces_list
        )

    def surface_area(self):
        """Возвращает площадь поверхности куба"""
        return sum(self.faces_list)


class Triangle:
    """
    Класс фигуры треугольник.
    Arg:
        base_length - длина основания
        height - высота треугольника (перпендикуляр от вершины к основанию)
    Arguments:
        __base_length - инкапсулированная длина основания
        __height - инкапсулированная высота треугольника
    """

    def __init__(self, base_length: float, height: float) -> None:
        self.base_length = base_length
        self.height = height

    @property
    def base_length(self) -> float:
        """Геттер длины основания"""
        return self.__base_length

    @base_length.setter
    def base_length(self, new_base_length) -> None:
        """Сеттер длины основания"""
        self.__base_length = new_base_length

    @property
    def height(self) -> float:
        """Геттер высоты треугольника"""
        return self.__height

    @height.setter
    def height(self, new_height) -> None:
        """Сеттер высоты треугольника"""
        self.__height = new_height

    def square(self) -> float:
        """Возвращает площадь треугольника"""
        return self.base_length / 2 * self.height

    def perimeter(self) -> float:
        """Возвращает периметр треугольника"""
        thigh_length = math.sqrt((1 / (self.base_length ** 2)) + (self.height ** 2))
        return thigh_length * 2 + self.__base_length


class Pyramid(Triangle, Square):
    """
    Класс описывающий фигуру пирамида. Порядок наследования важен!!!
        Arg:
        base_length - длина ребра квадрата в основании
        pyramid_height - высота пирамиды
    Arguments:
        faces_list - список площадей граней и основания пирамиды (основание последнее)
    """
    def __init__(self, base_length, pyramid_height):
        height_triangle = math.sqrt((base_length / 2) ** 2 + pyramid_height)       # высота триугольника(грани пирамиды)
        Triangle.__init__(self, base_length=base_length, height=height_triangle)   # инициализация наследодателю Triangle
        Square.__init__(self, length=base_length)                                  # инициализация наследодателю Square
        self.pyramid_height = pyramid_height
        self.faces_list = [round(self.square(), 3) for _ in range(4)]           # добавление площадей граней прирамиды
        self.faces_list.append(self.base_length ** 2)                           # добавление площади основания

    def __str__(self):
        """Представление экземпляра, возвращает строку с описанием"""
        return 'Пирамиды с высотой {} и длинной ребра основания {}\nсписок площадей граней: {}'.format(
            round(self.height, 3),
            round(self.pyramid_height, 3),
            self.faces_list
        )

    def surface_area(self):
        """Возвращает площадь поверхности пирамиды"""
        return sum(self.faces_list)


cube_1 = Cube(length=3)
print(cube_1)
print('Площадь поверхности куба: ', cube_1.surface_area())
pyramid_1 = Pyramid(base_length=10, pyramid_height=15)
print(pyramid_1)

