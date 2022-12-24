# Виталий Милентьев

# С помощью функции map выведите список имен с заглавной буквы.
# Результат: [‘Alfred’, ‘Tabitha’, ‘William’, ‘Arla’]
#
# PS. Используйте функцию написанную через def, затем Лямбда-функцию.
# Урок 10, дз №1
names = ['alfred', 'tabitha', 'william', 'arla']
def upperlist(list1):
    list2 = []
    for i in list1:
        list2.append(i.capitalize())
    return list2


print(upperlist(names))
list3 = list(map(lambda name1: name1.capitalize(), names))
print(list3)
# С помощью функции filter выведите список оценок, которые больше 75.
# Результат: [90, 76, 88, 81]
#
# PS. Сначала используйте функцию, объявленную с помощью def, а затем воспользуйтесь Лямбда-функцией.
# Урок 10, дз №2
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def bolshe(list1):
    list3 = []
    for i in list1:
        if i > 75:
            list3.append(i)
    return list3


print(bolshe(scores))
def bolshe1(zz):
    return zz > 75
list4 = list(filter(bolshe1, scores))
print(list4)

list5 = list(filter(lambda x: x > 75, scores))
print(list5)

# С помощью функции filter и Лямбда-функции выведите список слов-палиндромов.
#
# Результат: [‘Anna’, ‘Alla’, ‘Kazak’]
# Урок 10, дз №3

words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']

def palindrome_name(text1):
    return text1.lower() == text1[::-1].lower()


words2 = list(filter(palindrome_name, words))
print(words2)
words3 = list(filter(lambda text2: text2.lower() == text2[::-1].lower(), words))
print(words3)

# Напишите две функции (с генератором и без), которые будут формировать два списка: list1 — это список четных
# чисел и list2 — это список не четных чисел. Диапазон от 1 до n (n – это число, которое ввел юзер). Затем напишите
# к ней декоратор, который будет выводить время потраченное на выполнение работы функции, а также размер списка,
# который она сформировала.
# Урок 10, дз №4

from datetime import datetime
def performance(object):
    def cover():
        start = datetime.now()
        der = object()
        stop = datetime.now()
        print(stop - start)
        return der
    return cover


def chetnum(num1):
    num1 = int(num1)
    list1 = []
    for i in range(num1):
        if i % 2 == 0:
            list1.append(i)
    return list1

def nechetnum(num1):
    num1 = int(num1)
    list2 = []
    for i in range(num1):
        if i % 2:
            list2.append(i)
    return list2

z: int = input(f'Число: ')
print(chetnum(z))
print(nechetnum(z))

def chetnum1(num1):
    num1 = int(num1)
    list1 = [i for i in range(num1) if i % 2 == 0]
    return list1

def nechetnum1(num1):
    num1 = int(num1)
    list2 = [i for i in range(num1) if i % 2]
    return list2

print(chetnum1(z))
print(nechetnum1(z))

# Есть список слов. Нужно с помощью map и lambda функции вернуть список длин этих слов.
# Результат: [5, 6, 6]
# Урок 10, дз №5

text1 = ('apple', 'banana', 'cherry')

text2 = list(map(len, text1))

print(text2)

# Есть два текстовых списка. Нужно вернуть один список объединенных слов.
#
# Подаваемые данные: 2 списка
# Результат:
# [‘appleorange’, ‘bananalemon’, ‘cherrypineapple’]
# Урок 10, дз №6

text3 = ['apple', 'banana', 'cherry']
text4 = ['orange', 'lemon', 'pineapple']

text5 = []
for i in range(len(text3)):
    text5.append(text3[i] + text4[i])

print(text5)

# *** (Для Системных/Сетевых инженеров) Переделать скрипт для пинга, чтоб можно было передавать разные
# сетки или диапазоны, например:
#
# python ping_script 192.168.20.25 10.10.0.8
# или
# python ping_script 192.168.0.0/24 10.10.10.0/24 172.16.90.128/26
# Урок 10, дз №7



# *** (Для Системных/Сетевых инженеров) Написать IP калькулятор
#
# 10.176.0.0/14 — Network
# 255.252.0.0 — Mask
# 0.3.255.255 — Wildcard
#
# 10.176.0.1 — FistHost
# 10.179.255.254 — LastHost
# 10.179.255.255 — Broadcast
# Урок 10, дз №8

