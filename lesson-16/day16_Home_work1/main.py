from bs4 import BeautifulSoup
import time
from pprint import pprint
from configs import *
from base_parser import BaseParser
from mixin import ProductDetailMixin



class CategoryParser(BaseParser, ProductDetailMixin):
    def __init__(self):
        super(CategoryParser, self).__init__()
        self.DATA = {}

    def category_block_parser(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        category_links = soup.find_all('div', class_="offer-wrapper")
        # print(category_links)
        cnt = 1
        for i in category_links[:2]:
            link_o = i.find('a', class_=["marginright5", "link"]).get('href')
            mesto_vremya_o = i.find('td', class_='bottom-cell').get_text(strip=True)
            opisanie_o = i.find('h3', class_=["lheight22", "margintop5"]).get_text(strip=True)
            price_o = i.find('p', class_='price').get_text(strip=True)
            img_link_o = i.find('img', class_='fleft').get('src')
            self.DATA = {
                f'id_{cnt}': {},
            }
            self.DATA[f'id_{cnt}'] = {
                'opisanie_o': opisanie_o,
                'price_o': price_o,
                'link_o': link_o,
                'img_link_o': img_link_o,
                'mesto_vremya_o': mesto_vremya_o,
                'polnoe_o': None
            }
            cnt += 1
            # pprint(self.DATA)
            # print(link_o)
            category_page = self.get_html(link_o)
            time.sleep(3)
            self.category_page_parser(category_page, cnt)
            pprint(self.DATA)

        # for category in category_links[:3]:
        #     category_title = category.find('h2', class_='content__title').get_text(strip=True)
        #     print(style.BLUE + category_title)
        #     time.sleep(5)
        #     self.DATA[category_title] = []
        #     category_link = self.host + category.get('href')
        #     print(category_link)
        #
        #     category_page = self.get_html(category_link)
        #     self.category_page_parser(category_page, category_title)

    def category_page_parser(self, category_page, cnt):
        soup = BeautifulSoup(category_page, 'html.parser')
        ul_list = soup.find_all('ul')
        li_all = ul_list[1].find_all('li')
        category_title = []
        # print(len(ul_list))
        for i in li_all:
            category_title.append(i.get_text(strip=True))
        self.DATA[f'id_{cnt-1}']['polnoe_o'] = category_title
        # section = soup.find('div', class_='catalog-content__products')
        # products = section.find_all('div', class_='product-item-wrapper')
        # for product in products[:3]:
        #     product_name = product.find('a', class_='product-name').get_text(strip=True)
        #     product_price = product.find('div', class_='f-16').get_text(strip=True)
        #
        #     print(style.YELLOW + product_name)
        #     print(product_price)
        #     product_link = self.host + product.find('a', class_='product-link').get('href')
        #     product_detail_page = self.get_html(product_link)
        #     characteristics = self.get_detail_info(product_detail_page)
        #     self.DATA[category_title].append({
        #         'Имя продукта': product_name,
        #         'Цена продукта': product_price,
        #         'Ccылка на продукт': product_link,
        #         'Характеристики': characteristics
        #     })


def start_category_parsing():  # telefony
    category_link = HOST
    parser = CategoryParser()
    category_link1 = parser.get_html(category_link)
    soup = BeautifulSoup(category_link1, 'html.parser')
    catalog1 = soup.find('div', class_='maincategories')
    # pprint(catalog1)
    section = catalog1.find_all('div', class_='item')
    spoler = catalog1.find_all('ul')


    catalog_dic = []
    cnt = 1
    cnt1 = 1
    # print(spoler[0])
    for i in section:
        try:
            name = i.find('a', class_=['link', 'parent']).get_text(strip=True).lstrip('Просмотреть все объявления')
            if len(name) == 0:
                pass
            else:
                id_g = str(cnt)
                link_g = i.find('a', class_=['link', 'parent']).get('href')
                c_id = i.find('a', class_=['link', 'parent']).get('data-id')
                catalog_dic.append(id_g)
                catalog_dic[cnt-1] = {
                    'id': id_g,
                    'name': name,
                    'linkg': link_g,
                    'catalog_id': c_id,
                    'catalog_p': []
                }
                print(f'{id_g} {name}')

                spoler1 = spoler[cnt - 1].find_all('li')
                cnt += 1
                for z in spoler1:
                    if len(z.get_text(strip=True)) == 0:
                        pass
                    else:
                        id_p = str(cnt1)
                        name1_p = z.find('a', class_='link-relatedcategory').get_text(strip=True)
                        link_p = z.find('a', class_='link-relatedcategory').get('href')
                        c_id_p = z.find('a', class_='link-relatedcategory').get('data-id')
                        # print(z.get_text(strip=True).split('\n'))
                        cnt1 += 1
                        catalog_dic[cnt - 2]['catalog_p'].append({'id': id_p, 'name': name1_p, 'linkg': link_p, 'catalog_id': c_id_p})
                cnt1 = 1
        except AttributeError:
            pass

    parser = CategoryParser()
    category = input("Введите название категории: ")
    if 0 < int(category) <= len(catalog_dic):
        for i in catalog_dic[int(category)-1]["catalog_p"]:
            print(f"{i['id']} {i['name']}")
    else:
        pass
    category2 = input("Введите название категории: ")
    print(f'{"="*30}   {"="*30}')
    category_link = catalog_dic[int(category)-1]["catalog_p"][int(category2)-1]['linkg']
    # print(style.RED + 'Парсер начал работу')
    # # start = time.time()
    #
    html = parser.get_html(category_link)
    time.sleep(3)
    parser.category_block_parser(html)
    # parser.save_data_to_json(category, parser.DATA)
    # #print(html)
    #
    # # finish = time.time()
    # print(style.GREEN + f'Парсер завершил работу за время {round(finish - start, 2)} сек')


if __name__ == '__main__':
    start_category_parsing()
