# Виталий Милентьев

# Напишите программу, которая спрашивает имя пользователя и затем приветствует его.
# Урок 1, дз №1

name = input("Введите имя: ")
print(f"Привет, {name}")

# Напишите программу, которая считывает три числа и выводит их сумму.
# Урок 1, дз №2

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
print(f"Сумма чисел {num1}, {num2} и {num3} равно ", num1+num2+num3)

# Напишите программу, для решения следующей задачи: n школьников делят k яблок поровну, неделящийся остаток остается
# в корзинке. Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке? Программа получает на
# вход числа n и k и должна вывести искомое количество яблок (два числа).
# Урок 1, дз №3

school = int(input("Введите число школьников: "))
apple = int(input("Введите число яблок: "))
received = apple // school
remains = round(apple % school,1)
print(f"Каждому досталось {received} яблок, осталось в корзине {remains}")

# v2

school = int(input("Введите число школьников: "))
apple = int(input("Введите число яблок: "))
received = apple // school
remains = round(apple % school,1)
print(f"Каждому досталось {received} яблок, осталось в корзине {remains}")

# Напишите программу, которая спрашивает число у пользователя и выводит следующее:
# Урок 1, дз №4

num1 = int(input("Введите число: "))
print(f"Следущее число для {num1} --> ", num1+1, f"\nПредыдущее число для {num1} --> ", num1-1)

# Напишите программу, которая выводит текст в данном формате
# Урок 1, дз №5

print(f"Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\t\tUp above the world so high,\n\t\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are ")

# Напишите программу для использования метода форматирования следующих трех переменных в соответствии с ожидаемым результатом.
# Урок 1, дз №6

totalMoney = 1000
quantity = 3
price = 450
print(f"У меня есть {totalMoney} долларов, поэтому я могу купить {quantity} футбольных мяча за {price} долларов")

# Создайте две переменных, со значением ‘spam’ и ‘eggs’, затем распечатайте объединив две переменной в одну целую
# Урок 1, дз №7

variable1 = "spam"
variable2 = "eggs"
print(variable1 + variable2)