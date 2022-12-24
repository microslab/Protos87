# Виталий Милентьев

# Словари (Dict)
# Есть два словаря, объедините их:
# Урок 6, дз №1.1

dict1 = {
    'meat': 90,
    'milk': 15,
    'bread': 3,
    'potato': 6,
    'apple': 20,
    'banana': 25,
    'chicken wings': 45,
    'chocolate': 17
}
dict2 = {
    'kiwi': 30,
    'orange': 25,
    'coca-cola': 10,
    'chips': 18
}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

# Напишите сценарий Python для создания и печати словаря, содержащего число (от 1 до n включительно)
# (где n — введенное пользователем число) в форме (x, x * x).
# Урок 6, дз №2.1

n = int(input('Введите число: '))
num1 = {i: i * i for i in range(1,n+1)}
print(num1)

# Напишите код для суммирования всех значений словаря и вывод среднего арифметического значения.
# Урок 6, дз №3.1

n = int(input('Введите число: '))
num1 = {i: i * i for i in range(1,n+1)}
print(f'Сумма всех значений: {sum(num1.values())}')
print(f'Среднее арифметическое: {(sum(num1.values()))/(len(num1))}')

# Напишите код для объединения двух списков в словарь ключ: значение. СПИСКИ ДОЛЖНЫ БЫТЬ ОДНОГО РАЗМЕРА
# (содержимое списков произвольный)
# Урок 6, дз №4.1
# v1

list1 = ['management', 'sales', 'hr', 'production', 'admins']
list2 = ['vlan10', 'vlan20', 'vlan30', 'vlan40', 'vlan50']
print(f'Список1: {list1}')
print(f'Список2: {list2}')
n = len(list1)
dict1 = {}
for i in range(n):
    dict1[list1[i]] = list2[i]
print(f'Объединенный словарь: {dict1}')

# v2

list1 = ['management', 'sales', 'hr', 'production', 'admins']
list2 = ['vlan10', 'vlan20', 'vlan30', 'vlan40', 'vlan50']
n = len(list1)
n2 = len(list2)
dict1 = {}
if n == n2:
    for i in range(n):
        dict1[list1[i]] = list2[i]
    print(f'Список1: {list1}')
    print(f'Список2: {list2}')
    print(f'Объединенный словарь: {dict1}')
else:
    print('СПИСКИ ДОЛЖНЫ БЫТЬ ОДНОГО РАЗМЕРА!')

# Есть словарь координат городов:
# Урок 6, дз №5.1

cities = {
'Moscow': (550, 370),
'London': (510, 510),
'Paris': (480, 480),
}

distances = {}
moscow = cities['Moscow']
london = cities['London']
paris = cities['Paris']

for i in cities:
    if i == 'Moscow':
        n = (((moscow[0] - london[0])**2) + ((moscow[1] - london[1])**2))**0.5
        distances.update({'Moscow-London': round(n, 4)})
    if i == 'London':
        n = (((london[0] - paris[0])**2) + ((london[1] - paris[1])**2))**0.5
        distances.update({'London-Paris': round(n, 4)})
    if i == 'Paris':
        n = (((moscow[0] - paris[0])**2) + ((moscow[1] - paris[1])**2))**0.5
        distances.update({'Moscow-Paris': round(n, 4)})
distances = dict(sorted(distances.items()))
print(distances)

# Кортежи (tuple)/Множества (set)
# Есть кортеж a = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
#
# Выведите в отдельный кортеж числа, которые меньше или равны 5 и числа, которые больше 5.
# Урок 6, дз №1.2

a = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
a = list(a)
b = []
c = []
for i in a:
    if i > 5:
        c.append(i)
    else:
        b.append(i)
b = tuple(b)
c = tuple(c)
print(f'Кортеж чисел меньше или равных 5 {b}')
print(f'Кортеж чисел больше 5 {c}')

# Вы принимаете от пользователя его имя, фамилию, возраст. Сохраните их в соответствующие переменные. Сохраните
# полученные значения в список.
# Урок 6, дз №2.2

list1 = []
list2 = ['Введите ваше имя: ', 'Введите вашу фамилию: ', 'Ведите ваш возраст: ']
while len(list1) < 3:
    list1.append(input(f'{list2[len(list1)]}'))
list1 = tuple(list1)
print(f'Кортеж данных пользователя: {list1}')

# Напишите программу, которая принимает от пользователя секвенцию чисел, разделенных запятой и пробелом. После чего
# запишите каждое число в кортеж.
# Урок 6, дз №3.2

list1 = []
print(f'Введите секвенцию чисел, разделенных запятой и пробелом. \nНапример: 10, 15, 20')
num1 = str(input('Введите числа: '))
num1 = num1.replace('.', ',')
list1 = num1.replace(' ', '').split(',')
list1 = tuple(list1)
print(f'Кортеж чисел: {list1}')

# Напишите программу, которая будет принимать три имени в качестве входных данных от пользователя в одном input()
# и превращать данные в кортеж, ну а затем доставать их:
# Урок 6, дз №4.2

list1 = []
list2 = ['Первое имя: ', 'Второе имя: ', 'Третье имя: ']
num1 = 0
text1 = input("Введите три Имени: ")
if (len(text1.split())) == 3:
    list1 = text1.split()
    list1 = tuple(list1)
    print(f'Кортеж имен: {list1}')
    for i in list1:
        print(f'{list2[num1]}{i}')
        num1 += 1
else:
    print("Вы ввели не правильно, нужно три имя")

# Дан кортеж чисел numbers = (1, 2, 3, 4, 5, 6, 7). напишите программу, которая превращает каждый элемент кортежа
# в его квадрат и образует второй кортеж.
# Урок 6, дз №5.2

numbers = (1, 2, 3, 4, 5, 6, 7)
print(f'Кортеж чисел: {numbers}')
numbers = list(numbers)
num1 = 0
for i in numbers:
    numbers[num1] = (i**2)
    num1 += 1
numbers = tuple(numbers)
print(f'Кортеж Квадратов: {numbers}')

# Напишите программу, которая выводит все четные числа из кортежа в исходном порядке, и останавливается когда
# число равно 815.
# Урок 6, дз №6.2

numbers = (386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918,
           237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81,
           379, 843, 831, 445, 742, 717, 958,743, 527)
numbers = list(numbers)
list1 = []
for i in numbers:
    if i % 2 == 0 and i < 815:
        list1.append(i)
num1 = 0
for a in list1:
    num1 = num1 + a
numbers = tuple(numbers)
list1 = tuple(list1)
print(f'Оригинальный список: {numbers}')
print(f'Новый: {list1}')
print(f'Суммв нового списка {num1}')

# Есть кортеж с данными numbers = (12, 33, 44, 33, 12, 45, 11, 55, ’44’, 30, 10), создайте список и кортеж данных без дубликатов
# Урок 6, дз №7.2
# v1

numbers = (12, 33, 44, 33, 12, 45, 11, 55, '44', 30, 10)
list1 = []
for x in numbers:
    if x not in list1:
        list1.append(x)
print(list1)
list1 = tuple(list1)
print(list1)

# v2
numbers = (12, 33, 44, 33, 12, 45, 11, 55, '44', 30, 10)
numbers = list(set(numbers))
print(numbers)
numbers = tuple(numbers)
print(numbers)

# Получите кортеж VLANов со строки:
#     общих vlan
#     vlan которые есть в config_sw1 но нет в config_sw2
#     уникальные vlan c двух сторон
#     все vlan без дубликатов
# Урок 6, дз №8.2

config_sw1 = 'switchport trunk allowed vlan 10,20,30,40,50,70'
config_sw2 = 'switchport trunk allowed vlan 80,90,10,45,50,100'
while config_sw1.find('  ') != -1:
    config_sw1 = config_sw1.replace("  ", " ")
list1 = config_sw1.split(' ')
list2 = list1[-1].split(',')
list2 = set(list2)
while config_sw2.find('  ') != -1:
    config_sw2 = config_sw2.replace("  ", " ")
list3 = config_sw2.split(' ')
list4 = list3[-1].split(',')
list4 = set(list4)
print(tuple(list2.intersection(list4)))
print(tuple(list2.difference(list4)))
print(tuple(list2.symmetric_difference(list4)))
print(tuple(list2.union(list4)))
# или
tuple1 = tuple(list2.intersection(list4))
tuple2 = tuple(list2.difference(list4))
tuple3 = tuple(list2.symmetric_difference(list4))
tuple4 = tuple(list2.union(list4))
print(f'{tuple1}\n{tuple2}\n{tuple3}\n{tuple4}')

# Вложенность
# В задании создан словарь, с информацией о разных устройствах.
#
# Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1). И вывести информацию о
# соответствующем устройстве
# Урок 6, дз №1.3

devices = {
    'r1': {
        'location': 'Bukhara',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': 'Samarkand',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': 'Tashkent',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
n = ''
for i in devices:
    n = n + i + ' '
n = n.replace(' ', '/')[:-1]
list1 = ['Расположен:', 'Вендор:', 'Модель:', 'Система (ios):', 'IP адрес:', 'vlans:', 'Маршрутизация:']
n1 = 0
num1 = input(f'Введите название Устройства [{n}]: ')
num2 = '{:<25} {:20}'
for i in devices[num1]:
    line1 = num2.format(f'{list1[n1]}', f'{devices[num1][i]}')
    n1 += 1
    print(f'{line1}')

# Есть словарь кодов товаров и словарь количества товара на складе, задача сопоставить два словаря и высчитать
# общее количество.
# Урок 6, дз №2.3

goods = {
 'Лампа': '12345',
 'Стол': '23456',
 'Диван': '34567',
 'Стул': '45678',
}
store = {
 '12345': [
  {
   'quantity': 27,
   'price': 42
  },
 ],
 '23456': [
  {
   'quantity': 22,
   'price': 510
  },
  {
   'quantity': 32,
   'price': 520
  },
],
 '34567': [
  {
   'quantity': 2,
   'price': 1200
  },
  {
   'quantity': 1,
    'price': 1150
  },
 ],
 '45678': [
  {
   'quantity': 50,
   'price': 100
  },
  {
   'quantity': 12,
   'price': 95
  },
  {
   'quantity': 43,
   'price': 97
  },
 ],
}

n = ''
for i in goods:
    n = n + i + ' '
n = n.split()

n1 = ''
for x in store:
    n1 = n1 + x + ' '
n1 = n1.split()
z = 0
y = 0
for c in n1:
    for x in store[c]:
        z = z + x["quantity"]
        y = y + (x["quantity"] * x["price"])
    print(f'Продукт: {n[n1.index(c)]}, Количество {z}, Стоимость: {y}')
    z = 0
    y = 0