# Виталий Милентьев

# В примере найти и вывести трехзначные числа с помощью регулярных выражений.
# Урок 12, дз №1

import re
sample = 'Exercises number 1, 12, 13, and 345 are important 456 4564 456 131564 258'
sample2 = re.findall(r'\b\d{3}\b', sample)

print(sample2)

# Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF, то есть # и содержит затем 6
# шестнадцатеричных символов.
# Урок 12, дз №2

import re
collors = ['#ABCDEF', '#54#', '#F08080', '#FA8072', 'fghw3d', '#8B0000', 'A#8B0000', 'A0#8B0000', '#8B0000A', '#8B00003']
collors2 = []

for i in collors:
    if re.search(r'\B#[0-9A-Fa-f]{6}\b', i):
        collors2.append(i)
    else:
        pass

print(collors2)

# Найти в тексте время. Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00. Напишите
# регулярное выражение для поиска времени в строке: «Завтрак в 09:00». Учтите, что «37:98» – некорректное время.
# Урок 12, дз №3

import re
text = ['Завтрак в 09:00', 'Завтрак в 90:00', 'Обед  в 13:00', 'Обед в 13:61', 'Ужин в 19:05', 'Ужин в 37:98',
        'Ужин в 24:01']
text2 = []
for i in text:
    z = re.findall(r'\d{2}:\d{2}', i)
    for x in z:
        z2 = x.split(':')
    if int(z2[0]) < 24 and int(z2[1]) < 60:
        text2.append(i)
    else:
        pass

print(text2)

# Создать запрос для выбора из текста дробных чисел с разделителем дробной части в виде точки. Разряды целой части
# могут не выделяться или отделяться пробелом или запятой. 1231.12313
# Урок 12, дз №4

import re
numbers = [1231.12313, 2121.121, 3.14, 6598, 9898787, 999.99, '098 90', '123,123']
numbers1 = []
numbers2 = []


def text1(i, type2):
    z = str(i)
    x = re.findall(r'\d+\.\d+', z)
    if x:
        return numbers2.append(type2(x[0]))
    else:
        return numbers1.append(type2(z))


for i in numbers:
    if type(i) == int:
        type1 = int
        text1(i, type1)
    elif type(i) == str:
        type1 = str
        text1(i, type1)
    elif type(i) == float:
        type1 = float
        text1(i, type1)

print(numbers1)
print(numbers2)

# ** Добавить регулярное выражения для поиска и вывода MAC адресов в скрипте который работал с конфигурациями
# маршрутизатора (можно переделать весь скрипт для работы с регуляркой)
# Урок 12, дз №5

import re
inter = []

with open('files/show_ip_interface.txt') as file9:
    list1 = file9.read().split('\n')
    for i in list1:
        for z in list1:
            if len(z) < 1:
                list1.remove('')

        if re.findall(r'[up]{2}', i):
            i_name = i.split()[0].split('(')[0] + ' '
            inter.append(i_name)
for i in inter:
    if i == ' ':
        inter.remove(i)
# print(inter)
info = {}
with open('files/show_interface.txt') as file10:
    for line_number, line in enumerate(file10, 1):
        for interface in inter:

            if interface in line:
                info[interface] = {'start': line_number}

            elif len(line.strip()) == 0:
                if info.get(interface) and not info[interface].get('stop'):
                    info[interface]['stop'] = line_number


with open('files/show_interface.txt') as file11:
    for line_number, line in enumerate(file11, 1):
        for i in info.values():
            start, stop = i['start'], i['stop']
            if start <= line_number <= stop:
                if re.findall(r'Description:', line) and len(line.split(':')) > 1:
                    i['desc'] = line.split(':')[-1].rstrip('\n')
                elif re.findall(r'Internet Address is', line):
                    if not i.get("ip"):
                        i["ip"] = [line.split()[-1]]
                    else:
                        i["ip"].append(line.split()[-2])
                elif re.findall(r'Hardware address is', line):
                    i["mac"] = line.split()[-1]
                elif re.findall(r'According to flow,Maximal BW', line):
                    i['bw'] = line.split()[8].rstrip(',')
                elif re.findall(r'Rx Power', line):
                    i['rx'] = line.split()[2].rstrip(',')
                elif re.findall(r'Tx Power', line):
                    i['tx'] = line.split()[2].rstrip(',')
                elif re.findall(r'Encapsulation dot1q Virtual LAN', line):
                    i['Vlan'] = line.split()[-1]



with open('info_done.txt', 'w') as file12:
    file12.write(f'{"Name Interface":30} {"IP address":38} {"VLan":5} {"BW":5} {"RX":10} {"TX":10} '
                 f'{"MAC address":20} {"Description"}\n\n')
    for key in info:
        int_name = key
        ip = '; '.join(info[key].get("ip", "NA"))
        desc = info[key].get('desc', 'NA')
        bw = info[key].get("bw", "NA")
        rx = info[key].get("rx", "NA")
        tx = info[key].get("tx", "NA")
        mac = info[key].get("mac", "NA")
        vlan = info[key].get("Vlan", "NA")

        file12.write(f'{int_name:30} {ip:38} {vlan:5} {bw:5} {rx:10} {tx:10} {mac:20} {desc}\n')

# С сайта https://jsonplaceholder.typicode.com/
#
# a) На основе WEB ресурса Создать свои JSON файлы
# b) c JSON файлов переделать данные в формат CSV файла
# с) с CSV файла обратно конвертировать данные в JSON формат и создать файл
# Урок 12, дз №6

import requests
from pprint import pprint
import json
import csv

host = 'https://jsonplaceholder.typicode.com/users'
host2 = 'https://jsonplaceholder.typicode.com/posts'
host3 = 'https://jsonplaceholder.typicode.com/comments'
host4 = 'https://jsonplaceholder.typicode.com/albums'
host5 = 'https://jsonplaceholder.typicode.com/photos'
host6 = 'https://jsonplaceholder.typicode.com/todos'
users = requests.get(host).json()
posts = requests.get(host2).json()
comments = requests.get(host3).json()
albums = requests.get(host4).json()
photos = requests.get(host5).json()
todos = requests.get(host6).json()

posts2 = []
comments2 = []
albums2 = []
photos2 = []
todos2 = []
for post in posts:
    title = post['title']
    body = post['body']
    id1 = int(post['userId'])-1
    user = users[id1]['name']

    posts2.append({
        'Юзер': user,
        'Заголовок': title,
        'Текст': body
    })

for comment in comments:
    name = comment['name']
    email = comment['email']
    body = comment['body']

    comments2.append({
        'Имя': name,
        'Почта': email,
        'Текст': body
    })

for album in albums:
    title = album['title']
    id1 = int(album['userId'])-1
    user = users[id1]['name']

    albums2.append({
        'Юзер': user,
        'Текст': title
    })

for photo in photos:
    title = photo['title']
    url = photo['url']
    thumbnailUrl = photo['thumbnailUrl']

    photos2.append({
        'Юзер': title,
        'Ссылка на фото': url,
        'Ссылка на миниатюру': thumbnailUrl
    })

for todo in todos:
    title = todo['title']
    id1 = int(todo['userId'])-1
    user = users[id1]['name']
    completed = todo['completed']

    todos2.append({
        'Юзер': user,
        'Текст': title,
        'Выполнено': completed
    })

with open('posts2.json', mode='w',  encoding='UTF-8') as file:
    json.dump(posts2, file, ensure_ascii=False, indent=4)
with open('comments2.json', mode='w', encoding='UTF-8') as file:
    json.dump(comments2, file, ensure_ascii=False, indent=4)
with open('albums2.json', mode='w', encoding='UTF-8') as file:
    json.dump(albums2, file, ensure_ascii=False, indent=4)
with open('photos2.json', mode='w', encoding='UTF-8') as file:
    json.dump(photos2, file, ensure_ascii=False, indent=4)
with open('todos2.json', mode='w', encoding='UTF-8') as file:
    json.dump(todos2, file, ensure_ascii=False, indent=4)

# ** У системного/сетевого администратора есть инструмент мониторинга сети PRTG (Графическое отображения только
# для примера )
# Администратор сгенерировал с системы мониторинга отчет о трафике в файлах формата CSV и XML, и теперь необходимо:
#
# a) С файла historicdata.csv вытащить все значения поля «Traffic In (speed)», выяснить максимум и минимум трафика,
# а так же конвертировать значения в читабельный вид (дано в kbit/s, нужен вид в Gbit/s или Mbit/s в зависимости
# от читабельности)
#
# b) С файла historicdata.xml вытащить все значения поле «Traffic Out (volume)», выяснить максимум и минимум трафика,
# а так же конвертировать значения в читабельный вид (дано в KByte, нужен вид в GByte или MByte в зависимости
# от читабельности)
# Урок 12, дз №7

# Не успел прочитать

#
# Урок 12, дз №8



#
# Урок 12, дз №9



#
# Урок 12, дз №10



#
# Урок 12, дз №11


