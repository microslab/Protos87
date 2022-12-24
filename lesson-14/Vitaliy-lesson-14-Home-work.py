# Виталий Милентьев

# Создать Класс животное с одним параметром (по схеме)
#
#     от него унаследовать четыре подкласса с уникальными параметрами
#     затем создать по два объекта (экземпляра) от каждого подкласса
# Урок 14, дз №1

class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Класс Animal с полями: name={self.name}'

    def say_about_you(self):
        return f'Животное с названием {self.name}'


class Birds(Animal):
    def __init__(self, name, color, mesto, razmerkrila, eda):
        Animal.__init__(self, name)
        self.color = color
        self.mesto = mesto
        self.razmerkrila = razmerkrila
        self.eda = eda

    def __str__(self):
        return f'Класс Birds с полями: name={self.name}, color={self.color}, mesto={self.mesto}, razmerkrila={self.razmerkrila}, eda={self.eda}'

    def say_about_you(self):
        return f'Животное с названием {self.name} цвет {self.color} место обитания {self.mesto} размах крыла {self.razmerkrila} еда {self.eda}.'


class Mammals(Animal):
    def __init__(self, name, color, mesto, razmer, eda):
        Animal.__init__(self, name)
        self.color = color
        self.mesto = mesto
        self.razmer = razmer
        self.eda = eda

    def __str__(self):
        return f'Класс Mammals с полями: name={self.name}, color={self.color}, mesto={self.mesto}, razmer={self.razmer}, eda={self.eda}'

    def say_about_you(self):
        return f'Животное с названием {self.name} цвет {self.color} место обитания {self.mesto} размер {self.razmer} еда {self.eda}.'

class Reptiles(Animal):
    def __init__(self, name, mesto, razmech, razmer, eda):
        Animal.__init__(self, name)
        self.mesto = mesto
        self.razmech = razmech
        self.razmer = razmer
        self.eda = eda

    def __str__(self):
        return f'Класс Reptiles с полями: name={self.name}, mesto={self.mesto}, razmech={self.razmech}, razmer={self.razmer}, eda={self.eda}'

    def say_about_you(self):
        return f'Животное с названием {self.name} место обитания {self.mesto} размер чешуи {self.razmech} размер {self.razmer} еда {self.eda}.'

class Fish(Animal):
    def __init__(self, name, mesto, color, eda):
        Animal.__init__(self, name)
        self.mesto = mesto
        self.color = color
        self.eda = eda

    def __str__(self):
        return f'Класс Fish с полями: name={self.name}, mesto={self.mesto}, color={self.color}, eda={self.eda}'

    def say_about_you(self):
        return f'Животное с названием {self.name} место обитания {self.mesto} цвет {self.color} еда {self.eda}.'



orel = Birds('Орел', 'Серый', 'Горы', '3 м', 'Мясо')
kurica = Birds('Курица', 'Белый', 'Курятник', '40 см', 'Корм')

krisa = Mammals('Крыса', 'Черный', 'подвал', '30 см', 'обьедки')
obezyana = Mammals('Обезьяна', 'Коричневый', 'зоопарк', '65 см', 'Корм')

zmeya = Reptiles('Змея', 'Лес', '3 см', '5 м', 'Дичь')
hamelion = Reptiles('Хамелион', 'Разный', '1 см', '40 см', 'Корм')

ribakloun = Fish('Рыба-Клоун', 'Пресный водоем', 'Оранжевый с белым', 'Корм')
belakula = Fish('Белая акула', 'Океан', 'Серый', 'Рыбы')

print(orel.say_about_you())
print(kurica.say_about_you())
print(krisa.say_about_you())
print(obezyana.say_about_you())
print(zmeya.say_about_you())
print(hamelion.say_about_you())
print(ribakloun.say_about_you())
print(belakula.say_about_you())

# Создать класс Фигура с одним параметром (по схеме),
#
#     от него унаследовать три подкласса с уникальными параметрами
#     в каждом подклассе создать полезные методы
#     Решить двумя способами, с помощью полиморфизма и без него
#
# подобное вы уже должны были делать на 12 задании, тут тоже самое только в классах
# Урок 14, дз №2


class Figures:
    def __init__(self, name):
        self.name = name

class Circle(Figures):
    def __init__(self, name, radius, Pi=3.14):
        Figures.__init__(self, name)
        self.radius = radius
        self.Pi = Pi

    def circle_perimeter(self):
        P = 2 * self.Pi * self.radius
        return round(P, 3)

    def circle_area(self):
        S = self.Pi * (self.radius ** 2)
        return round(S, 3)

class Square(Figures):
    def __init__(self, name, side_a, side_b):
        Figures.__init__(self, name)
        self.side_a = side_a
        self.side_b = side_b

    def square_perimeter(self):
        P = 2 * (self.side_a + self.side_b)
        return P


    def square_area(self):
        S = self.side_a * self.side_b
        return S

class Triangle(Figures):
    def __init__(self, name, side_a, side_b, side_c):
        Figures.__init__(self, name)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def triangle_perimeter(self):
        P = (self.side_a + self.side_b + self.side_c) / 2
        return round(P, 3)


    def triangle_area(self):
        P = self.triangle_perimeter()
        S = (P * (P - self.side_a) * (P - self.side_b) * (P - self.side_c)) ** 0.5
        return round(S, 3)

# from Название скрипта import Circle, Triangle, Square // from Название скрипта import *

krug = Circle('Круг', 5)
treug = Triangle('Треугольник', 5, 4, 3)
chetir = Square('Четырехугольник', 5, 4)
print(krug.circle_area())
print(krug.circle_perimeter())
print(treug.triangle_area())
print(treug.triangle_perimeter())
print(chetir.square_area())
print(chetir.square_perimeter())