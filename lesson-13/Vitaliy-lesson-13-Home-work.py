# Виталий Милентьев

# В примере найти и вывести трехзначные числа с помощью регулярных выражений.
# Урок 13, дз №1

from functools import total_ordering


@total_ordering
class Pc_info:

    def __init__(self, name, cp, ram, hdd, screen):
        self.name: str = name
        self.cp: str = cp
        self.ram: int = ram
        self.hdd: int = hdd
        self.screen: str = screen
        self.say_who_am_i()

    def user_name(self):
        return self.name

    def pc_cp(self):
        return self.cp

    def pc_ram(self):
        return self.ram

    def pc_hdd(self):
        return self.hdd

    def pc_srcreen(self):
        return self.screen

    def __str__(self):
        return f"Класс Pc_info c полями:\nname(Имя Владельца) = {self.name}\ncp(Имя процессора)= {self.cp}\n" \
               f"ram(Обьем памяти в Гигобайтах)= {self.ram}\nhdd(Объём жесткого диска в Гигобайтах)= {self.hdd}\n" \
               f"screen(Например: '27 дюймов')= {self.screen}"

    def __eq__(self, other):
        return self.ram == other.ram

    def __lt__(self, other):
        return self.ram < other.ram

    def say_who_am_i(self):
        print(f'Владелец PC зовут: {self.name}')


user_pc1 = Pc_info('Vasya', 'i7', 16, 500, '27 дюймов')
user_pc2 = Pc_info('Petya', 'i5', 32, 1000, '32 дюймов')

print()
print(user_pc1.screen)
print()
print(user_pc2.hdd)
print()
print(user_pc1 == user_pc2)
print(user_pc1 > user_pc2)
print(user_pc1 >= user_pc2)
print(user_pc1 < user_pc2)
print(user_pc1 <= user_pc2)
print()
print(user_pc1)
print(user_pc2)

