# Виталий Милентьев

# В кругу стоят n человек, пронумерованных числами от 1 до n. Начинается расчет, при котором каждый k-й по счету
# человек выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу,
# определяющую номер человека, который останется в кругу последним
#
# Пример: В кругу 9 человек, убывает каждый 3тий, на первом проходе уйдет человек под номером 3, затем 6, затем 9,
# затем 4, затем 8,  затем 5, затем 2, затем 7, последним останется человек под номером 1
# Урок 4, дз №1

# v new
num1 = 9
for i in range(1, num1+1):
     for j in range(i, i*num1+1, i):
         print(j, end='\t')
     print()

# v old
#
# num1 = int(input('Введите количество человек: '))
# number = int(input('Какой по счету человек будет выбывать из круга: '))
# print(f'Значит, выбывает каждый {number} человек.')
# num_list = list(range(1, num1 + 1))
# num2 = 0
# for i in range(num1 - 1):
#    start_num = num2 % len(num_list)
#    num2 = (start_num + number - 1) % len(num_list)
#    num_list.remove(num_list[num2])
# print('Остался человек под номером', num_list[0])



# Составить программу, которая спрашивает возраст человека и, если ему 18 лет и больше, сообщает “Замечательно.
# Вы уже можете водить автомобиль”, а в противном случае – “К сожалению, водить автомобиль Вам рановато”.
# (так же можете сами придумать и добавить вывод сообщения в зависимости от возраста)
# Урок 4, дз №2

num3 = True
while num3:
    num1 = input('Ведите ваш возраст: ')
    num2 = num1.isdigit()
    if num2:
        num1 = int(num1)
        if num1 < 25:
            print('К сожалению, водить автомобиль Вам рановато')
        else:
            print('Замечательно. Вы уже можете водить автомобиль')
    else:
        print('Это не возраст')
    num4 = input('Продолжить [ Y/N ]: ')
    num4 = num4.lower()
    if num4 == 'n':
        num3 = False
print('Выход')

# Создайте игру «Угадай число», программа генирирует рандомное число в заданном интервале, и предлагает пользователю
# угадать, игра продолжается до тех пор пока пользователь угадает число, пример игры на картинке ниже:
# Урок 4, дз №3

import random
name1 = 'Python'
print(f'{name1}: Привет, как тебя зовут?')
name2 = input('Ваше имя: ')
name2 = name2.capitalize()
print(f'{name1}: Что ж, {name2}, я загадываю число от 1 до 5.')
print(f'{name1}: Попробуй угодать')
num1 = True
num3 = random.randint(1, 5)
x = 0
while num1:
    num2 = input(f'{name2}: ')
    if num2.isdigit():
        num2 = int(num2)
        if num2 < num3:
            print(f'{name1}: Твое число слишком маленькое')
            x += 1
        if num2 > num3:
            print(f'{name1}: Твое число слишком большое')
            x += 1
        if num2 == num3:
            x += 1
            print(f'{name1}: Отлично, {name2}! Ты справился за {x} попыток')
            num1 = False
    else:
        print(f'{name1}: {name2} Вы вели не число')

print(f'{name1}: Хочеш второй уровень?')
num1 = True
rand1 = random.randint(1, 10)
rand2 = random.randint(1, 50)
z = 0
num3 = False
num4 = False
v = 0
y = 0
c = 0
while num1:
    if z == 1:
        print(f'{name1}: Хочеш третий уровень?')
    num2 = input('Продолжить [ Y/N ]: ')
    num2 = num2.lower()
    if num2 == 'n':
        num1 = False
    if num2 == 'y' and z == 0:
        print(f'{name1}: Что ж, {name2}, я загадываю число от 1 до 10.')
        num3 = True
    if num2 == 'y' and z == 1 and c == 0:
        print(f'{name1}: Что ж, {name2}, я загадываю число от 1 до 50.')
        num4 = True
        while num4:
            num2 = input(f'{name2}: ')
            if num2.isdigit():
                num2 = int(num2)
                if num2 < rand2:
                    print(f'{name1}: Твое число слишком маленькое')
                    y += 1
                if num2 > rand2:
                    print(f'{name1}: Твое число слишком большое')
                    y += 1
                if num2 == rand2:
                    y += 1
                    print(f'{name1}: Отлично, {name2}! Ты справился за {y} попыток')
                    num4 = False
                    num1 = False
            else:
                print(f'{name1}: {name2} Вы вели не число')
    else:
        while num3:
            num2 = input(f'{name2}: ')
            if num2.isdigit():
                num2 = int(num2)
                if num2 < rand1:
                    print(f'{name1}: Твое число слишком маленькое')
                    v += 1
                if num2 > rand1:
                    print(f'{name1}: Твое число слишком большое')
                    v += 1
                if num2 == rand1:
                    v += 1
                    print(f'{name1}: Отлично, {name2}! Ты справился за {v} попыток')
                    z = 1
                    num3 = False
            else:
                print(f'{name1}: {name2} Вы вели не число')
numnum = '='
print(f'{name1}: {numnum*30}')
if x > 0 and v == 0 and y == 0:
    print(f'{name1}: Легкий уровень пройден за {x} попыток')
    print(f'{name1}: Обшее число попыток: {x + y + v}')
elif x > 0 and v > 0 and y == 0:
    print(f'{name1}: Легкий уровень пройден за {x} попыток')
    print(f'{name1}: Средний уровень пройден за {v} попыток')
    print(f'{name1}: Обшее число попыток: {x + y + v}')
else:
    print(f'{name1}: Легкий уровень пройден за {x} попыток')
    print(f'{name1}: Средний уровень пройден за {v} попыток')
    print(f'{name1}: Тяжелой уровень пройден за {y} попыток')
    print(f'{name1}: Обшее число попыток: {x + y + v}')
print(f'{name1}: Выход')


# Многие спортсмены жаловались, что судья слишком тихо отсчитывает секунды, оставшиеся до старта
# («Три!.. Два!.. Один!..»). Фирма Go Ahead купила табло для наглядного отображения оставшегося времени.
# Урок 4, дз №4

import datetime
import time

data = int(input("Укажите время для таймера (в минутах): "))
data = data * 60
for i in reversed(range(data+1)):
    result = datetime.timedelta(seconds=data)
    print(f"\r{result}",  end='', flush=True )
    time.sleep(1)
    data -= 1

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е.
# билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая выводит на экран
# все доступные счастливые билеты с подсчетом их количество
# Урок 4, дз №5

x = 0
y = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for f in range(10):
                    for g in range(10):
                        if (a + b + c) == (d + f + g):
                            x = x + 1
                            y = y + 1
                            print(f'Счастливый билет №{x}: {a} {b} {c}  {d} {f} {g}')
                        y = y + 1
print(f'Количество счастливых билетов: {x}')
z = round(x / (y / 100), 2)
print(f'Всего: {z} %')

# Нарисуйте ёлку (вид ёлки произвольный, на картинке только пример) , высоту ёлки должен задавать пользователь
# Урок 4, дз №6

num1 = input('Ведите высоту ёлки: ')
num2 = 0
num3 = '**'
num4 = ' '
num5 = num1
if num1.isdigit():
    num1 = int(num1)
    num5 = int(num5)
    for i in range(0, num1 + 1):
        num4 = num4 * num5
        num3 = num3 * num2
        print(f'{num4}{num3}{num4}', end='')
        num2 += 1
        num3 = '**'
        num5 -= 1
        num4 = ' '
        print()
else:
    print('Вы вели не целое число.')

# Написать программу «Банк». Вводится сумма вклада и количество лет. Рассчитать сколько денег будет на счету
# пользователя к концу времени вклада. Решить задачу по системе «сложный процент» (процент рассчитывается от новой
# суммы) Годовой процент считать равным 10%.
# Урок 4, дз №7

num1 = input('Введите сумму вклада: ')
num2 = input('Введите количество лет для вклада: ')
num3 = (num1.isdigit() and num2.isdigit())
if num3:
    num1 = int(num1)
    num2 = int(num2)
    for i in range(num2):
        num1 = ((num1 * 0.1) + num1)
        print(f'{i+1} год: {num1} $')
    print(f'За {num2} лет вы соберете: {num1} $')
else:
    print('Вы вели не целое число.')

# v2

num1 = input('Введите сумму вклада: ')
num2 = input('Введите количество лет для вклада: ')
num3 = input('Введите процент (например 10 или 5): ')
num4 = (num1.isdigit() and num2.isdigit() and num3.isdigit())
if num4:
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    num3 = num3 / 100
    for i in range(num2):
        num1 = ((num1 * num3) + num1)
        print(f'{i+1} год: {int(num1)} $')
    print(f'За {num2} лет вы соберете: {int(num1)} $')
else:
    print('Вы вели не целое число.')

# Задача «Лесенка» По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел
# от 1 до i без пробелов.
# Урок 4, дз №8

num1 = input('Введите количество лесенок: ')
num2 = 1
num3 = 1
if num1.isdigit():
    num1 = int(num1)
    for i in range(1, num1 + 1):
        for j in range(0, num2):
            print(num3, end='')
            if num3 >= 9:
                num3 = 0
            else:
                num3 += 1
        num2 += 1
        num3 = 1
        print()
else:
    print('Вы вели не целое число.')

# Последовательность Фибоначчи — это серия чисел. Следующее число находится путем сложения двух чисел перед ним.
# В первые два числа 0 и 1.
# Например, 0 + 1 = 1
# Урок 4, дз №9

num1 = input('Введите конечный номер Фибоначи: ')
num2 = 0
num3 = 1
if num1.isdigit():
    num1 = int(num1)
    for i in range(1, num1 + 1):
        print(f'{num2}', end=' ')
        num2, num3 = num3, num2 + num3
else:
    print('Вы вели не целое число.')