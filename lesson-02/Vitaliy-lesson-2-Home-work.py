# Виталий Милентьев

# Составить три формы присвоение следующего вида x, y, z = y, z, x (придумать способ применения )
# Урок 2, дз №1
# v1
x = 1
y = 2
z = 3
x, y, z = y, z, x
print(f'x = {x}')
print(f'y = {y}')
print(f'z = {z}')

# v2
x, y, z = 1, 2, 3
q, w, e = x, y, z
x, y, z = w, e, q
print(f'x = {x}\ny = {y}\nz = {z}')

# v3
x, y, z = 1, 2, 3
q = x
x, y, z = y, z, q
print(f'x = {x}\ny = {y}\nz = {z}')

# Распечатать: сложение, вычитание, умножение, деление, возведение в степень следующих переменных:
# Урок 2, дз №2

num1 = 3.14
num2 = 4
print(f'{num1} + {num2} = {round(num1 + num2,2)}')
print(f'{num1} - {num2} = {round(num1 - num2,2)}')
print(f'{num1} * {num2} = {round(num1 * num2,2)}')
print(f'{num1} / {num2} = {round(num1 / num2,3)}')
print(f'{num1} ** {num2} = {round(num1 ** num2,2)}')


# Воспользуйтесь различными методами строк
# Урок 2, дз №3
str1 = ' << pYthOn -   '
str2 = '   pYthOn \n .   '
str3 = ' (( pYthOn - :+   '

print(str1.replace(' ', '').strip('<-').lower())
print(str2.replace(' ', '').replace('\n', '').strip('-.').upper())
print(str3.replace(' ', '').strip('(-:+').lower())


# Обработайте каждую переменную и получите результат как на картинке:
# Урок 2, дз №4
# v1
string1 = 'I love python'
string2 = 'Hello my dear friend'
string3 = 'полиморфизм'
num1 = string2.find('my')
num2 = string2.find('friend')
print(string1[::-1])
print(string2[num1:num1+2:] + string2[num2-1::])
print(string3[::2])

# v2
string1 = 'I love python'
string2 = 'Hello my dear friend'
string3 = 'полиморфизм'
num1 = string2.split(' ')
print(string1[::-1])
print(num1[1],  num1[3])
print(string3[::2])


# С помощью метода строк Замените слово show на display и создайте другую переменную
# Урок 2, дз №5
show = 'show ip interface brief'
show2 = show.replace('show', 'display')

print(show)
print(show2)


# В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. Напишите программу, которая определяет
# номер купе, в котором находится место с заданным номером (нумерация мест сквозная, начинается с 1).
# Урок 2, дз №6

mest = 4
mest1 = int(input('Введите номер места, а я отвечу в каком купе он находится: '))
kupe1 = mest1 // mest
kupe2 = mest1 % mest
kupe3 = kupe2 == 0
kupe4 = str(kupe3)
kupe5 = int(kupe4.replace('False', '1').replace('True', '0'))
print(f'Место под номером {mest1} находится в {kupe1 + kupe5} купе')

# Как же трудно было придумать как без if тут обойтись. когда на работе всегда отвлекают )