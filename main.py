from pprint import pprint

import requests
import json


def print_max_intelligence(final_dict):
    hero = final_dict
    for k, v in hero.items():
        print(f'Максимальный интелект у героя {k} равен {v}')


def get_max_intelligence(intelligence):
    max_intelligence = max(intelligence.values())
    final_dict = {k: v for k, v in intelligence.items() if v == max_intelligence}
    # print(final_dict)
    print_max_intelligence(final_dict)


def get_data(name):
    url = "https://superheroapi.com/api/2619421814940190/search/"
    # params = {'name': 'Hulk'}
    heros = name
    keys_ = []
    values_ = []
    for hero in heros:
        response = requests.get(url + '/' + hero)
        datas = response.json()
        for data in datas['results']:
            keys_.append(data['name'])
            values_.append(int(data['powerstats']['intelligence']))
    dict_intelligence = dict(zip(keys_, values_))
    # print(dict_intelligence)
    get_max_intelligence(dict_intelligence)


if __name__ == '__main__':
    name = ['Hulk', 'Captain America', 'Thanos']
    # get_data(name)
