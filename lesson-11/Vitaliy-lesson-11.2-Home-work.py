# Виталий Милентьев

# *** (Для Системных/Сетевых инженеров) Переделать скрипт для пинга, чтоб можно было передавать разные сетки или диапазоны, например:
#
# python ping_script 192.168.20.25 10.10.0.8
#
# или
#
# python ping_script 192.168.0.0/24 10.10.10.0/24 172.16.90.128/26
# Урок 11.2, дз №1

# Если будет время попробую доделать пока работает только на последний актет

from ping3 import ping

def ip_sep(var):
    min, max = var.split('-')
    min, max = min.split('.'), max.split('.')
    lan = ''
    for i in range(len(min)-1):
        lan = lan + str(min[i]) + '.'
    for i in range(int(min[-1]), int(max[-1])+1):
        myping(lan + str(i))


def myping(var: str):
    resp = str(ping(var, timeout=0.1))
    if resp != 'False' and resp != 'None':
        print(f"{var} - Up")
    else:
        print(f"{var} - Down")


def main():
    strin1 = input("Введите адреса четвертого октета через провел: ")

    true_false = list(map(lambda item: '-' in item, strin1.split()))
    true_false_ip = list(zip(true_false, strin1.split()))

    for key, value in true_false_ip:
        if key:
            ip_sep(value)
        else:
            myping(value)


if __name__ == '__main__':
    main()

# (Для Системных/Сетевых инженеров) Написать IP калькулятор
# 10.176.0.0/14 — Network
# 255.252.0.0 — Mask
# 0.3.255.255 — Wildcard
#
# 10.176.0.1 — FistHost
# 10.179.255.254 — LastHost
# 10.179.255.255 — Broadcast
# Урок 11.2, дз №2

def main():
    print(f'Введите ip адресс. Напривет \033[31m192.168.0.1/24\033[39m или \033[31m192.168.0.1 255.255.255.0\033[39m')
    host1 = input('Введите ip адресс: ')
    ip_mask(host1)


def ip_mask(var):
    mask = {0: ['0.0.0.0', 4294967294, 'A'], 1: ['128.0.0.0', 2147483646, 'A'], 2: ['192.0.0.0', 1073741822, 'A'],
            3: ['224.0.0.0', 536870910, 'A'], 4: ['240.0.0.0', 268435454, 'A'], 5: ['248.0.0.0', 134217726, 'A'],
            6: ['252.0.0.0', 67108862, 'A'], 7: ['254.0.0.0', 33554430, 'A'], 8: ['255.0.0.0', 16777214, 'A'],
            9: ['255.128.0.0', 8388606, 'B'], 10: ['255.192.0.0', 4194302, 'B'], 11: ['255.224.0.0', 2097150, 'B'],
            12: ['255.240.0.0', 1048574, 'B'], 13: ['255.248.0.0', 524286, 'B'], 14: ['255.252.0.0', 262142, 'B'],
            15: ['255.254.0.0', 131070, 'B'], 16: ['255.255.0.0', 65534, 'B'], 17: ['255.255.128.0', 32766, 'C'],
            18: ['255.255.192.0', 16382, 'C'], 19: ['255.255.224.0', 8190, 'C'], 20: ['255.255.240.0', 4094, 'C'],
            21: ['255.255.248.0', 2046, 'C'], 22: ['255.255.252.0', 1022, 'C'], 23: ['255.255.254.0', 510, 'C'],
            24: ['255.255.255.0', 254, 'C'], 25: ['255.255.255.128', 126, 'C'], 26: ['255.255.255.192', 62, 'C'],
            27: ['255.255.255.224', 30, 'C'], 28: ['255.255.255.240', 14, 'C'], 29: ['255.255.255.248', 6, 'C'],
            30: ['255.255.255.252', 2, 'C'], 31: ['255.255.255.254', 0, 'C'], 32: ['255.255.255.255', 0, 'C']}
    if bool(' ' in var):
        ip, mask1 = var.split()
        for i in mask:
            if str(mask[i][0]) == str(mask1):
                klass1 = mask[i][2]
                ip_ran = mask[i][1]
        ip_kalk(ip, mask1, ip_ran, klass1)
    elif bool('/' in var):
        ip, mask1 = var.split('/')
        ip_ran = str(mask[int(mask1)][1])
        klass1 = str(mask[int(mask1)][2])
        mask1 = mask[int(mask1)][0]
        print(klass1, ip_ran)
        ip_kalk(ip, mask1, ip_ran, klass1)


def ip_kalk(ip, mask, numb1, numb2):
    print(f'Ip: {ip}')
    print(f'Netmask: {mask}')
    mask1 = mask.split('.')
    ip1 = ip.split('.')
    Wildcard = ''
    Hostmin = ''
    Hostmax = ''
    for i in mask1:
        if bool(int(i) == 0):
            Wildcard = Wildcard + '255' + '.'
        elif bool(int(i) > 0):
            Wildcard = Wildcard + str(255 - int(i)) + '.'

    Wildcard = Wildcard.rstrip('.')
    print(f'Wildcard: {Wildcard}')
    num11 = Wildcard.split('.')
    cnt = 0
    for i in range(len(ip1)):
        if mask1[i] == '255':
            Hostmin = Hostmin + ip1[i] + '.'
            cnt += 1
        elif 0 < int(mask1[i]) < 255:
            Hostmin = Hostmin + ip1[i] + '.'
            cnt += 1
        elif mask1[i] == '0':
            if int(cnt) == int(len(ip1) - 1):
                Hostmin = Hostmin + '1' + '.'
                cnt += 1
            else:
                Hostmin = Hostmin + '0' + '.'
                cnt += 1
    Hostmin = Hostmin.rstrip('.')
    print(f'Hostmin: {Hostmin}')
    cnt = 0
    for i in range(len(ip1)):
        if mask1[i] == '255':
            Hostmax = Hostmax + ip1[i] + '.'
            cnt += 1
        elif 0 < int(mask1[i]) < 255:
            if int(int(ip1[i]) + int(num11[i])) > 255:
                Hostmax = Hostmax + '255' + '.'
            else:
                Hostmax = Hostmax + str(int(int(ip1[i]) + int(num11[i]))) + '.'
            cnt += 1
        elif mask1[i] == '0':
            if int(cnt) == int(len(ip1) - 1):
                Hostmax = Hostmax + '254' + '.'
                cnt += 1
            else:
                Hostmax = Hostmax + '255' + '.'
                cnt += 1
    Hostmax = Hostmax.rstrip('.')
    print(f'Hostmax: {Hostmax}')
    cnt = 0
    num22 = Hostmax.split('.')
    Broadcast = ''
    for i in range(int(len(Hostmax))):
        if int(cnt) == (int(len(num22)) - 1):
            Broadcast = Broadcast + str(int(num22[i]) + 1) + '.'
            cnt += 1
        elif cnt > 3:
            break
        else:
            Broadcast = Broadcast + num22[i] + '.'
            cnt += 1
    Broadcast = Broadcast.rstrip('.')
    print(f'Broadcast: {Broadcast}')
    print(f'Class: Class {numb2}')
    print(f'Hosts: {numb1}')



if __name__ == '__main__':
    main()
