import requests
from configs import *
import json


class BaseParser:
    def __init__(self):
        self.url = URL
        self.host = HOST

    def get_html(self, link):
        HEADER = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
        }
        return requests.get(link, HEADER).text

    @staticmethod
    def save_data_to_json(path, data):
        with open(f"{path}.json", mode='w', encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

