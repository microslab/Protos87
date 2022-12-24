# Виталий Милентьев

# Домашняя работа:
#
# https://www.gazeta.ru/
# Урок 15, дз №1.1
import requests, unicodedata, json, re
from pprint import pprint
from bs4 import BeautifulSoup

HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
HOST = 'https://www.gazeta.ru'
CATEGORY = []
html = requests.get(HOST, headers=HEADER).text
soup = BeautifulSoup(html, 'html.parser')
categori = soup.find_all('div', class_='b_nav')
categor2 = soup.find_all('div', class_='b_menu-content')
regex = r"\"\/\D*\/\""
cnt = 1
for i in categori[0]:
    if str(i.get_text(strip=True)) != '':
        name_ru = i.get_text(strip=True)
        name_link = i.get('href')
        CATEGORY.append({
            'id': cnt,
            'name_ru': name_ru,
            'name_link': name_link
        })
        cnt += 1
    else:
        pass
for i in categor2[0]:
    if str(i.get_text(strip=True)) !='':
        name_ru = i.get_text(strip=True)
        name_link = re.findall(regex, str(i))
        name_link = name_link[0].strip('"')
        CATEGORY.append({
            'id': cnt,
            'name_ru': name_ru,
            'name_link': name_link
        })
        cnt += 1
    else:
        pass


print(f"Категории для парсинга")
for i in CATEGORY:
     print(f'{i["id"]}: {i["name_ru"]}')

number = input("Введите номер категории: ")

if number != '':
    for i in CATEGORY:
        if str(i['id']) == number:
            CATEGORY2 = i['name_link']
else:
    CATEGORY2 = '/news/'

CATEGORY3 = 'news/'
HOST2 = 'https://www.gazeta.ru' + CATEGORY2
html2 = requests.get(HOST2, headers=HEADER).text
soup = BeautifulSoup(html2, 'html.parser')
if soup.find('a', class_='b_newslist-showmorebtn'):
    HOST2 = HOST2 + CATEGORY3
    html2 = requests.get(HOST2, headers=HEADER).text
    soup = BeautifulSoup(html2, 'html.parser')
else:
    pass
declarations = soup.find_all('a', class_='b_ear')
time = ''
json_data = []
for i in declarations:
    try:
        image_link = i.find('img').get('src')
        title = i.find('div', class_='b_ear-title').get_text(strip=True)
        time = i.find('time', class_='b_ear-time').get_text(strip=True)
    except AttributeError:
        pass
    except NameError:
        image_link = i.find('img').get('src')
        title = i.find('div', class_='b_ear-title').get_text(strip=True)

    json_data.append({
        'title': unicodedata.normalize('NFKD', title),
        'time': unicodedata.normalize('NFKD', time),
        'image_link': image_link
    })

name_json = CATEGORY2.strip("/").split("/")[-1]
with open(f'gazeta_{name_json}.json', mode='w', encoding='UTF-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)