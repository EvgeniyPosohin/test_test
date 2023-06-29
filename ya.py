import requests
import os
from dotenv import load_dotenv, find_dotenv


class YaDirect:

    def __init__(self, token):
        self.token = token
        self.link_url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def is_path_exists(self, path):
        params = {'path': f'disk:/{path}'}
        response = requests.get(self.link_url, headers=self.get_headers(), params=params)
        if response.status_code == 200:
            return True
        return False

    def create_folder(self, path):
        params = {'path': f'disk:/{path}'}
        res = requests.put(self.link_url, headers=self.get_headers(), params=params)
        return res


load_dotenv(find_dotenv())
yandex = YaDirect(os.getenv('token_ya'))
