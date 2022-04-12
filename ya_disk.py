from pprint import pprint

import requests
import os

with open('token.txt', 'r') as f:
    token_YD = f.read().strip()


class YaUploader:

    def __init__(self, token):
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        self.url = "https://cloud-api.yandex.net/v1/disk/resources"

    def upload_file_to_disk(self, path_to_file):
        # формирование url
        upload_url = self.url + '/' + 'upload'
        # имя файла
        filename = path_to_file.split('\\')[-1]
        params = {"path": filename, "overwrite": "true"}
        # запрос получения сслки для загрузки
        response = requests.get(upload_url, headers=self.headers, params=params).json()
        # pprint(response)
        href = response['href']
        # Запрос на закрузку файла по загрузочной ссылке
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    uploader = YaUploader(token=token_YD)
    BASE_PATH = os.getcwd()
    FILE_DIR = 'test_dz.txt'
    path_to_file = os.path.join(BASE_PATH, FILE_DIR)
    # print(path_to_file.split('\\')[-1])
    result = uploader.upload_file_to_disk(path_to_file)
