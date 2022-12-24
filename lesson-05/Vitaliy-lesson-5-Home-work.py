# Виталий Милентьев

# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Выведите в отдельный список числа, которые меньше или равны 5 и числа, которые больше 5.
# Урок 5, дз №1

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []
for i in a:
    if i <= 5:
        b.append(i)
    else:
        c.append(i)
print(f'Оригенальный лист:          | {a}')
print(f'Список меньше или равны 5:  | {b}')
print(f'Список больше 5:            | {c}')

# Вы принимаете от пользователя его имя, фамилию, возраст. Сохраните их в соответствующие переменные.
# Сохраните полученные значения в список.
# Урок 5, дз №2

list1 = []

num1 = str(input('Введите ваше имя: '))
num2 = str(input('Введите вашу фамилию: '))
num3 = str(input('Ведите ваш возраст: '))

list1.append(num1)
list1.append(num2)
list1.append(num3)
print(list1)

# v2
list1 = []
list2 = ['Введите ваше имя: ', 'Введите вашу фамилию: ', 'Ведите ваш возраст: ']
while len(list1) < 3:
    list1.append(input(f'{list2[len(list1)]}'))
print(list1)

# Напишите программу, которая принимает от пользователя секвенцию чисел, разделенных запятой и пробелом.
# После чего запишите каждое число в список.
# Урок 5, дз №3

list1 = []
print(f'Введите секвенцию чисел, разделенных запятой и пробелом. \nНапример: 10, 15, 20')
num1 = str(input('Введите числа: '))
num1 = num1.replace('.', ',')
list1 = num1.replace(' ', '').split(',')
print(list1)

# Напишите программу, которая принимает пример со СЛОЖЕНИЕМ у пользователя и затем выдает результат.
# (решите с помощью генератора списка)
# Урок 5, дз №4

# v1
list1 = []
print(f'Введите выражение. Например:\033[31m 10 + 15 - 20\033[39m')
num1 = str(input('Введите выражение: '))
num2 = ''

if num1.find('-') != -1:
    num1 = num1.replace('-', ' - ')
elif num1.find('+') != -1:
    num1 = num1.replace('+', ' + ')
elif num1.find('/') != -1:
    num1 = num1.replace('/', ' / ')
elif num1.find('*') != -1:
    num1 = num1.replace('*', ' * ')
elif num1.find('(') != -1:
    num1 = num1.replace('(', ' ( ')
elif num1.find(')') != -1:
    num1 = num1.replace(')', ' ) ')
while num1.find('  ') != -1:
    num1 = num1.replace("  ", " ")
list1 = num1.split(' ')
for i in list1:
    if i.isdigit() == 1:
        num2 = num2 + i
    else:
        num2 = num2 + i
num3 = eval(num2)
print(f'Выражение {num1} = {num3}')
print(f'Результат: {num3}')
# v2

print(f'Введите выражение. Например:\033[31m 10 + 15 - 20\033[39m')
num1 = str(input('Введите выражение: '))
if num1.find('-') != -1:
    num1 = num1.replace('-', ' - ')
elif num1.find('+') != -1:
    num1 = num1.replace('+', ' + ')
elif num1.find('/') != -1:
    num1 = num1.replace('/', ' / ')
elif num1.find('*') != -1:
    num1 = num1.replace('*', ' * ')
elif num1.find('(') != -1:
    num1 = num1.replace('(', ' ( ')
elif num1.find(')') != -1:
    num1 = num1.replace(')', ' ) ')
while num1.find('  ') != -1:
    num1 = num1.replace("  ", " ")
num2 = eval(num1)
print(f'Выражение {num1} = {num2}')
print(f'Результат: {num2}')

# Напишите программу, которая будет принимать три имени в качестве входных данных от пользователя
# в одном input() вызове функции.
# Урок 5, дз №5

# v1
list1 = []
text1 = input("Введите три Имени: ")
if (len(text1.split())) == 3:
    list1 = text1.split()
    print(f'Первое имя: {list1[0]}')
    print(f'Второе имя: {list1[1]}')
    print(f'Третье имя: {list1[2]}')
else:
    print("Вы ввели не правильно, нужно три имя")

# v2

list1 = []
list2 = ['Первое имя: ', 'Второе имя: ', 'Третье имя: ']
num1 = 0
text1 = input("Введите три Имени: ")
if (len(text1.split())) == 3:
    list1 = text1.split()
    for i in list1:
        print(f'{list2[num1]}{i}')
        num1 += 1
else:
    print("Вы ввели не правильно, нужно три имя")


# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7]. напишите программу, которая превращает каждый
# элемент списка в его квадрат.
# Урок 5, дз №6
# v1
numbers = [1, 2, 3, 4, 5, 6, 7]
list1 = []
for i in numbers:
    list1.append((i**2))
print(f'Список чисел: {numbers}')
print(f'Список Квадратов: {list1}')

# v2

numbers = [1, 2, 3, 4, 5, 6, 7]
print(f'Список чисел: {numbers}')
num1 = 0
for i in numbers:
    numbers[num1] = (i**2)
    num1 += 1
print(f'Список Квадратов: {numbers}')

# Создайте список из любимых вами блюд.
#   Создайте список из любимых блюд вашего друга, скопировав свой список.
#   Убедитесь что два списка разные, добавив по одному разному блюду в каждый список.
#   Выведите два списка.
# Урок 5, дз №7

list1 = ['Плов', 'Шашлык', 'Манты', 'Окрошка']
list2 = list1.copy()
list1.append('Блины')
list2.append('Сыр')
if id(list1) != id(list2):
    print(f'Список моих любимых блюд: {list1}')
    print(f'Список любимых блюд друга: {list2}')



# Создайте переменную user_num, которая будет принимать от пользователя число.
# Создайте числовой список от 1 до значения из переменной user_num (значение из переменной включительно).
# Выведите сам список и сумму его чисел.
# Урок 5, дз №8

user_num = input('Введите число: ')
num1 = user_num.isdigit()
num2 = 0
if num1:
    user_num = int(user_num)
    list1 = [i for i in range(1, user_num+1)]
    for a in list1:
        num2 = num2 + a
    print(f'Список чисел в диапазоне от 1 до {user_num}: {list1}')
    print(f'Сумма чисел равна: {num2}')
else:
    print('Вы вел не коректно. Введите одно число')

# Создайте два числовых списка от 1 до 100. Первый будет состоять только из четных чисел, а второй из нечётных.
# Выведите сам список и сумму его чисел.
# Урок 5, дз №9

num1 = 0
num2 = 0
list1 = [i for i in range(1, 101) if i % 2 == 0]
list2 = [i for i in range(1, 101) if i % 2 != 0]
for a in list1:
    num1 = num1 + a
for b in list2:
    num2 = num2 + b
print(f'Список четных чисел: {list1}')
print(f'Сумма четных чисел равна: {num1}')
print(f'Список нечетных чисел: {list2}')
print(f'Сумма нечетных чисел равна: {num2}')


# Напишите программу, которая выводит все четные числа из списка в исходном порядке, и останавливается
# когда число равно 815.
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918,
# 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843,
# 831, 445, 742, 717, 958,743, 527]
# Урок 5, дз №10

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237,
           412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379,
           843, 831, 445, 742, 717, 958,743, 527]
list1 = []
for i in numbers:
    if i % 2 == 0 and i < 815:
        list1.append(i)
num1 = 0
for a in list1:
    num1 = num1 + a
print(f'Оригинальный список: {numbers}')
print(f'Новый: {list1}')
print(f'Суммв нового списка {num1}')

# Подсчитайте общее количество цифр в числе.
# Например, число 75869 , поэтому на выходе должно быть 5.
# Урок 5, дз №11

num1 = input('Введите свое число: ')
num2 = num1.isdigit()
num3 = len(num1)
if num2:
    print(f'Кол-во цифр в числе {num1} равна {num3}')
else:
    print(f'Вы вели не число')

# Напишите программу для отображения всех простых чисел в диапазоне (Учтите что пользователь может ввести
# отрицательное число)
# (Для справки: Простое число — это число, которое нельзя получить путем умножения других целых чисел. Простое число —
# это натуральное число больше 1, которое не является произведением двух меньших натуральных чисел.
# Например:
#   — 6 не является простым числом, потому что его можно получить как 2 × 3 = 6
#   — 37 — простое число, потому что никакие другие целые числа не умножаются вместе, чтобы получить его.)
#   Учтите что пользователь может ввести отрицательное число
# Урок 5, дз №12

num1 = input('Введите положительный стартовый номер: ')
num2 = input('Введите положительный конечный номер: ')
num3 = (num1.replace('-', '').isdigit() and num2.replace('-', '').isdigit())
num4 = 0
list1 = []
if num3:
    num1 = int(num1)
    num2 = int(num2)
    if num1 <= 1:
        num1 = 2
    if num1 < num2:
        for i in range(num1, num2 + 1):
            for j in range(2, i):
                if i % j == 0:
                    num4 = num4 + 1
            if num4 == 0:
                list1.append(i)
            else:
                num4 = 0
    else:
        print(f'Второе число должно быть больше первого и положительное')
else:
    print('Вы вели не цифры')
for z in list1:
    print(z)

# Обработать строку ospf_route и вывести информацию на стандартный поток вывода как на картинке ниже:
#
# ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
# для практики возьмите список маршрутов со своего роутера и попробуйте преобразить вывод всех таблиц маршрутов
# Урок 5, дз №13

# v1
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
num1 = ospf_route
while num1.find('  ') != -1:
    num1 = num1.replace("  ", " ")
num1 = num1.replace(",", "")
list1 = num1.split(' ')
num2 = '\t'
print(f'''Protocol:{num2*4}OSPF
Network:{num2*4}{list1[1]}
AD/Metric:{num2*4}{list1[2]}
Next-Hop:{num2*4}{list1[4]}
Last update:{num2*3}{list1[5]}
Outbound Interface{num2*2}{list1[6]}''')

# v2
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
num1 = ospf_route
while num1.find('  ') != -1:
    num1 = num1.replace("  ", " ")
num1 = num1.replace(",", "")
list1 = num1.split(' ')
num2 = '{:<25} {:20}'
line1 = num2.format('Protocol:', 'OSPF')
line2 = num2.format('Network:', f'{list1[1]}')
line3 = num2.format('AD/Metric:', f'{list1[2]}')
line4 = num2.format('Next-Hop:', f'{list1[4]}')
line5 = num2.format('Last update:', f'{list1[5]}')
line6 = num2.format('Outbound Interface', f'{list1[6]}')
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
# или так
# print(f'{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}')

# Получите список VLANов со строки:
#
# config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
# Урок 5, дз №14

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
num1 = config
while num1.find('  ') != -1:
    num1 = num1.replace("  ", " ")
list1 = num1.split(' ')
list2 = list1[-1].split(',')
print(list2)