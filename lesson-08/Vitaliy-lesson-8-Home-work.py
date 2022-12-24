# Виталий Милентьев

#                   Работа с файлами
# Откройте файл mbox-short.txt, “прочитайте” каждую строку в этом файле и найдите строки, соответствующие данной:
# “From Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008” . Затем распечатайте все ВХОДЯЩИЕ email адреса и их
# общее количество. Для решения данной задачи используйте методы строк.
# Урок 8, дз №1

cnt = 0
with open('files/mbox-short.txt', encoding='UTF-8') as file1:
    for line in file1:
        if line.startswith('From '):
            email = line.split()[1]
            print(email)
            cnt += 1
print(f"Количество входящих писем: {cnt}")

# Откройте файл romeo.txt. “Прочитайте” в нем каждую строку. Получите отдельные слова из каждой строки, после чего
# составьте список слов. В списке слова не должны дублироваться. После чего распечатайте список, в котором все слова
# будут отсортированы в алфавитном порядке.
# Урок 8, дз №2

with open('files/romeo.txt', encoding='UTF-8') as file2:
    list1 = file2.read().split()
    list1 = sorted(list(set(list1)))
n = ((str(list1)[120:]).find(',')) + 1
print(f'{str(list1)[:120 + n]}\n{str(list1)[120 + n + 1:]}')

# Напишите код программы, которая будет открывать файл «article.txt» и выводить на печать построчно последние строки
# в количестве lines (число которую можно запросить у пользователя). Число должно быть положительным
# Урок 8, дз №3

with open('files/article.txt', encoding='UTF-8') as file3:
    list1 = file3.read().split('\n')
    for i in list1:
        if len(i) < 1:
            list1.remove('')

num1 = input('Сколько последних строк распечатать: ')
num2 = len(list1)
try:
    num1 = int(num1)
    num3 = num2 - num1
    if num1 < 0:
        print('Укажите положительное число!')
    elif num1 > num2:
        print('Вы указали слишком большое число!')
    elif num1 == 0:
        print(f'Вы указали {num1} в этом случае нету строк для вывода!')
    else:
        for i in list1[num3::]:
            print(i)
except ValueError:
    print('Укажите число!')

# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# Требуется реализовать код программы, которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).
# Урок 8, дз №4

with open('files/article.txt', encoding='UTF-8') as file4:
    list1 = file4.read().split()
max_len = max(list1, key=len)
print(f"Слова Имеющие максимальную длину: ['{max_len}']")

# Объедините содержимое файлов pushkin.txt, byron.txt, romeo.txt в один файл Poems.txt.
# # ** Разверните строки каждого стихотворения.
# # *** Постарайтесь придерживаться правильного выравнивание текста и чтоб знак «=>» вставлялся ровно посередине
# каждого стихотворения (добейтесь результата в точности как на картинке)
# Урок 8, дз №5

num1 = ''
with open('files/Poems.txt', 'w', encoding='UTF-8') as file5:
    with open('files/pushkin.txt', encoding='UTF-8') as file6:
        with open('files/byron.txt', encoding='UTF-8') as file7:
            with open('files/romeo.txt', encoding='UTF-8') as file8:
                stix1 = file6.read().split('\n')
                stix2 = file7.read().split('\n')
                stix3 = file8.read().split('\n')
                for i in stix3:
                    if len(i) < 1:
                        stix3.remove('')
                file5.write(f'{num1:50}-----{file6.name}-----\n')
                z = len(stix1) - 1
                x = (z + 1) // 2
                for i in stix1:
                    if z == x:
                        file5.write(f'{i:50}{num1:9}==>{num1:9}{stix1[z]:50}\n')
                        z -= 1
                    else:
                        file5.write(f'{i:50}{num1:21}{stix1[z]:50}\n')
                        z -= 1
                file5.write(f'\n{num1:50}-----{file7.name}-----\n')
                z = len(stix2) - 1
                x = (z + 1) // 2

                for i in stix2:
                    if z == x:
                        file5.write(f'{i:50}{num1:9}==>{num1:9}{stix2[z]:50}\n')
                        z -= 1
                    else:
                        file5.write(f'{i:50}{num1:21}{stix2[z]:50}\n')
                        z -= 1
                file5.write(f'\n{num1:50}-----{file8.name}-----\n')
                z = len(stix3) - 1
                x = (z + 1) // 2

                for i in stix3:
                    if z == x:
                        file5.write(f'{i:50}{num1:9}==>{num1:9}{stix3[z]:50}\n')
                        z -= 1
                    else:
                        file5.write(f'{i:50}{num1:21}{stix3[z]:50}\n')
                        z -= 1

# *** Собрать полезную информацию с конфигурационных файлов show_interface.txt show_ip_interface.txt
# Урок 8, дз №6

inter = []

with open('files/show_ip_interface.txt') as file9:
    list1 = file9.read().split('\n')
    for i in list1:
        for z in list1:
            if len(z) < 1:
                list1.remove('')
        # print(i.split()[-1])
        if i.split()[-1] == 'up':
            i_name = i.split()[0].split('(')[0] + ' '
            inter.append(i_name)

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
                if 'Description' in line and len(line.split(':')) > 1:
                    i['desc'] = line.split(':')[-1].rstrip('\n')
                elif 'Internet Address is' in line:
                    if not i.get("ip"):
                        i["ip"] = [line.split()[-1]]
                    else:
                        i["ip"].append(line.split()[-2])
                elif 'Hardware address is' in line:
                    i["mac"] = line.split()[-1]
                elif 'According to flow,Maximal BW' in line:
                    i['bw'] = line.split()[8].rstrip(',')
                elif 'Rx Power' in line:
                    i['rx'] = line.split()[2].rstrip(',')
                elif 'Tx Power' in line:
                    i['tx'] = line.split()[2].rstrip(',')
                elif 'Encapsulation dot1q Virtual LAN' in line:
                    i['Vlan'] = line.split()[-1]



with open('files/info_done.txt', 'w') as file12:
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
