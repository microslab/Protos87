# Виталий Милентьев

#                   break, continue, pass
# Есть список list1 = [i for i in range(100)], создайте новый список с пробросом каждого пятого элемента
# (используйте continue)
# Урок 7, дз №1

list1 = [i for i in range(100)]
list2 = []
for i in list1:
    if not ((i+1) % 5):
        continue
    else:
        list2.append(i)

# Напишите скрипт который будет работать циклично в интерактивном режиме, скрипт должен запрашивать имя пользователя,
# если пользователь не вводя имя нажмет на Enter то скрипт должен завершиться (используйте break)
# Урок 7, дз №2

while True:
    z = input('Ведите имя: ')
    if z == '':
        break
    else:
        print(f'Вы вели имя: {z}')

# Есть список: list1 = [‘micros’, ‘python’, ‘linux’, ‘windows’, ‘bobo’], из него составить новый список, но без
# буквы ‘i’, результат: list2 = [‘mcros’, ‘python’, ‘lnux’, ‘wndows’, ‘bobo’] (используйте pass)
# Урок 7, дз №3

list1 = ['micros', 'python', 'linux', 'windows', 'bobo']
list2 = []
y = ''
for i in list1:
    for z in i:
        if z == 'i':
            pass
        else:
            y = y + z
    list2.append(y)
    y = ''
print(list1)
print(list2)


#                   Try/except/finally/else
# Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом, то должна
# выполняться конкатенация, то есть соединение, строк. В остальных случаях введенные числа суммируются.
#
# Примеры выполнения программы:
# Первое значение: 4
# Второе значение: 5
# Результат: 9.0
# Первое значение: a
# Второе значение: 9
# Результат: a9
# Урок 7, дз №4

num1 = input('Ведите значение: ')
num2 = input('Ведите значение: ')
try:
    num1, num2 = float(num1), float(num2)
    num3 = num1 + num2
    z = 'Сумма чисел равна: '
except ValueError:
    num1, num2 = str(num1), str(num2)
    num3 = num1 + num2
    z = 'Сложение строк равно: '
print(f'{z}{num3}')

# Есть список: list1 = [1, ‘a’, 3, ‘b’, 5, ‘6’, 7, ‘8’, 9, ‘c’], необходимо разделить на два списка, в первом
# только цифровые значения, а во втором только строки
# Урок 7, дз №5

list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
list2 = []
list3 = []
for i in list1:
    if type(i) == int:
        list2.append(i)
    else:
        list3.append(i)
print(f'{list2}\n{list3}')


# Тот же самый пример, с сообщением после каждой итерации о том что элемент N добавлен
# Урок 7, дз №6

list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
list2 = []
list3 = []
for i in list1:
    if type(i) == int:
        print(f'Элемент списка {i} является {type(i)} и добавлин список с числами')
        list2.append(i)
    else:
        print(f'Элемент списка {i} является {type(i)} и добавлин список со строками')
        list3.append(i)
print(f'{list2}\n{list3}')

# Приведенный ниже код назначает 5-ю букву каждого слова в food новый список fifth. Однако код в настоящее время выдает
# ошибки. Вставьте предложение try/except, которое позволит запустить код и создать список 5-й буквы в каждом слове.
# Если слово недостаточно длинное, оно не должно ничего выводить. Примечание. pass — Оператор является нулевой
# операцией; ничего не произойдет при его выполнении.
# food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", “lemonade"]
# fifth = []
# for x in food:
#   fifth.append(x[4])
# Урок 7, дз №7

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []
for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        pass
print(fifth)

# Приведенный ниже код делит значения элемента на самого себя, но вылетает с ошибками, необходимо учесть все типы
# ошибок и дописать код (условия цикла менять нельзя, использовать полный синтаксис try/except/else)
# my_list = [2, "C", 10, "20", "micros", 50, 0, '0', '30']
# for index in range(len(my_list)+5):
#     print(my_list[index] / my_list[index])
# Урок 7, дз №8

my_list = [2, "C", 10, "20", "micros", 50, 0, '0', '30']
for index in range(len(my_list)+5):
    try:
        # print(my_list[index] / my_list[index])
        print(f'{my_list[index]} / {my_list[index]} = {my_list[index] / my_list[index]}')
        print(f'Все получилось так как элемент {my_list[index]} является числом')
    except TypeError:

        try:
            z = int(my_list[index])
            print(f"Ошибка ValueError c элементов '{my_list[index]}' является {type(my_list[index])}")
            print(f'{z} / {z} = {z / z}')
            print(f"Но я сконвертировал значение '{z}' так как тип элемента {type(my_list[index])}")
        except ZeroDivisionError:
            print(f'На ноль делить нельзя')
        except ValueError:
            print(f"Ошибка ValueError c элементов '{my_list[index]}' является {type(my_list[index])}")
    except ZeroDivisionError:
        print(f'На ноль делить нельзя')
    except IndexError:
        print(f'Список оказался слишком мал, индекс под номером {index} пуст')

# Дописать код (нельзя использовать просто except)
# my_dict ={"key1":"value1","key2":"value2","key3":"value3"}
# search_key = "non-existent key"
# print(my_dict[search_key])
# Урок 7, дз №9

my_dict ={"key1":"value1","key2":"value2","key3":"value3"}
search_key = "non-existent key"
try:
    print(my_dict[search_key])
except KeyError as keys:
    print(f"Сорян,'{keys}' это неправельный ключ")

# Замените первый if на try/except/else
# import sys
#
# if len(sys.argv) < 2:
#         print("Вы не указали название города")
#         print("Try again")
#         exit()
#
# city = sys.argv[1]
# city = city.lower()
#
#
# if city == "tashkent"[0:len(city)]:
#         print ("В Ташкенте тепло и солнечно")
# elif city == "london"[0:len(city)]:
#         print ("В Лондоне пасмурно и сыро")
# elif city == "moskow"[0:len(city)]:
#         print ("В Москве идёт сильный дождь")
# elif city == "paris"[0:len(city)]:
#         print ("погода для романтики")
# elif city == "rio de janeyro"[0:len(city)]:
#         print ("В Рио постоянно карнавалы")
#
# else:
#         print ("прогноз не ясен, карантин")
# Урок 7, дз № 10

import sys
try:
    city = sys.argv[1]
    city = city.lower()
except IndexError:
    print("Вы не указали название города")
    print("Try again")
    exit()

if city == "tashkent"[0:len(city)]:
        print ("В Ташкенте тепло и солнечно")
elif city == "london"[0:len(city)]:
        print ("В Лондоне пасмурно и сыро")
elif city == "moskow"[0:len(city)]:
        print ("В Москве идёт сильный дождь")
elif city == "paris"[0:len(city)]:
        print ("погода для романтики")
elif city == "rio de janeyro"[0:len(city)]:
        print ("В Рио постоянно карнавалы")
else:
        print ("прогноз не ясен, карантин")

# Следующий код работает отлично, если пользователь вводит цифровое значение, но всегда есть НО:
# min = int(input("Введите первое число: "))
# max = int(input("Введите второе число: "))
#
# for i in range(min, max+1):
#     print(f"Квадрат числа {i} равен {i*i}")
# Урок 7, дз № 11

try:
    min = int(input("Введите первое число: "))
    max = int(input("Введите второе число: "))
    if min > max:
        print('Перво число должно быть меньше второго')
    else:
        for i in range(min, max+1):
            print(f"Квадрат числа {i} равен {i*i}")
except ValueError:
    print('Вы вели не целое число')

# Ловить ошибки это конечно здорово, но уметь логировать их и записывать в файл еще лучше, задача разобраться со стандартной библиотекой logging
#
# Ниже пример:
# import logging # Загрузка библиотеки
#
# logging.basicConfig(filename='my_error.log') # Файл появится в том каталоге где запущен скрипт
# logger = logging
#
# try:
#     1/0
# except ZeroDivisionError as error:
#     logger.error(error)
#
# Результатом будет запись:
#
# ERROR:root:division by zero
# Урок 7, дз № 12.1


# a) Найдите способ чтоб можно было добавить время ошибки, например вот так:
# 2022-10-06 11:03:31,466 ERROR  division by zero

import logging # Загрузка библиотеки

logging.basicConfig(filename='my_error.log', format="%(asctime)s %(levelname)s  %(message)s") # Файл появится в том каталоге где запущен скрипт
logger = logging

try:
    1/0
except ZeroDivisionError as error:
    logger.error(error)

# b) Ко всем предыдущим примерам добавить логирования в файл
# ====================================
import logging # Загрузка библиотеки

logging.basicConfig(filename='my_error.log', format="%(asctime)s %(levelname)s  %(message)s") # Файл появится в том каталоге где запущен скрипт
logger = logging

num1 = input('Ведите значение: ')
num2 = input('Ведите значение: ')
try:
    num1, num2 = float(num1), float(num2)
    num3 = num1 + num2
    z = 'Сумма чисел равна: '
except ValueError as error:
    num1, num2 = str(num1), str(num2)
    num3 = num1 + num2
    z = 'Сложение строк равно: '
    logger.error(error)
print(f'{z}{num3}')

# ====================================

import logging # Загрузка библиотеки

logging.basicConfig(filename='my_error.log', format="%(asctime)s %(levelname)s  %(message)s") # Файл появится в том каталоге где запущен скрипт
logger = logging

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []
for x in food:
    try:
        fifth.append(x[4])
    except IndexError as error:
        logger.error(error)
        pass
print(fifth)
# ====================================

import logging # Загрузка библиотеки

logging.basicConfig(filename='my_error.log', format="%(asctime)s %(levelname)s  %(message)s") # Файл появится в том каталоге где запущен скрипт
logger = logging

my_list = [2, "C", 10, "20", "micros", 50, 0, '0', '30']
for index in range(len(my_list)+5):
    try:
        # print(my_list[index] / my_list[index])
        print(f'{my_list[index]} / {my_list[index]} = {my_list[index] / my_list[index]}')
        print(f'Все получилось так как элемент {my_list[index]} является числом')
    except TypeError as error:
        logger.error(error)

        try:
            z = int(my_list[index])
            print(f"Ошибка ValueError c элементов '{my_list[index]}' является {type(my_list[index])}")
            print(f'{z} / {z} = {z / z}')
            print(f"Но я сконвертировал значение '{z}' так как тип элемента {type(my_list[index])}")
        except ZeroDivisionError as error:
            logger.error(error)
            print(f'На ноль делить нельзя')
        except ValueError as error:
            logger.error(error)
            print(f"Ошибка ValueError c элементов '{my_list[index]}' является {type(my_list[index])}")
    except ZeroDivisionError as error:
        logger.error(error)
        print(f'На ноль делить нельзя')
    except IndexError as error:
        logger.error(error)
        print(f'Список оказался слишком мал, индекс под номером {index} пуст')

# ====================================

import logging # Загрузка библиотеки

logging.basicConfig(filename='my_error.log', format="%(asctime)s %(levelname)s  %(message)s") # Файл появится в том каталоге где запущен скрипт
logger = logging

my_dict ={"key1":"value1","key2":"value2","key3":"value3"}
search_key = "non-existent key"
try:
    print(my_dict[search_key])
except KeyError as keys:
    print(f"Сорян,'{keys}' это неправельный ключ")
    logger.error(keys)

# ====================================

import logging # Загрузка библиотеки
import sys

logging.basicConfig(filename='my_error.log', format="%(asctime)s %(levelname)s  %(message)s") # Файл появится в том каталоге где запущен скрипт
logger = logging


try:
    city = sys.argv[1]
    city = city.lower()
except IndexError as error:
    logger.error(error)
    print("Вы не указали название города")
    print("Try again")
    exit()

if city == "tashkent"[0:len(city)]:
        print ("В Ташкенте тепло и солнечно")
elif city == "london"[0:len(city)]:
        print ("В Лондоне пасмурно и сыро")
elif city == "moskow"[0:len(city)]:
        print ("В Москве идёт сильный дождь")
elif city == "paris"[0:len(city)]:
        print ("погода для романтики")
elif city == "rio de janeyro"[0:len(city)]:
        print ("В Рио постоянно карнавалы")
else:
        print ("прогноз не ясен, карантин")
# ====================================
import logging # Загрузка библиотеки

logging.basicConfig(filename='my_error.log', format="%(asctime)s %(levelname)s  %(message)s") # Файл появится в том каталоге где запущен скрипт
logger = logging


try:
    min = int(input("Введите первое число: "))
    max = int(input("Введите второе число: "))
    if min > max:
        print('Перво число должно быть меньше второго')
    else:
        for i in range(min, max+1):
            print(f"Квадрат числа {i} равен {i*i}")
except ValueError as error:
    logger.error(error)
    print('Вы вели не целое число')