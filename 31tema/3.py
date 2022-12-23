from typing import List
import requests
import json

def get_starship(starship_url: str, file_name: str) -> None:
    """
    Записывает в json файл данные о корабле
    :param starship_url: URL адрес корабля, который необходимо обработать
    :param file_name:Имя файла (обязательно формата .json), куда необходимо записать данные о корабле
    """
    starship_data = requests.get(starship_url)
    starship_info = json.loads(starship_data.text)
    result = {
        'ship_name': starship_info['name'],
        'starship_class': starship_info['starship_class'],
        'max_atmosphering_speed': starship_info['max_atmosphering_speed'],
        'pilots': get_pilots(starship_info),
    }
    print(result)
    with open(file_name, 'w') as file:
        json.dump(result, file, indent=4)


def get_pilots(starship_info: dict) -> List[dict]:
    """
    Получает данные о пилотах корабля
    :param starship_info: Словарь данных о корабле
    :return: Список всех пилотов корабля
    """
    result = []
    for p_url in starship_info['pilots']:
        pilot = requests.get(p_url)
        pilot_info = json.loads(pilot.text)
        result.append({
            'name': pilot_info['name'],
            'height': pilot_info['height'],
            'mass': pilot_info['mass'],
            'homeworld': json.loads(requests.get(pilot_info['homeworld']).text)['name'],
            'homeworld_url': pilot_info['homeworld']
        })
    return result

if __name__ == '__main__':
    get_starship('https://swapi.dev/api/starships/10/', 'millennium_falcon.json')
