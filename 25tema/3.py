class MyDict(dict):
    """
        Класс словаря. Родитель: dict
    """
    def get(self, key):
        """
            Возвращает элемент по ключу, если не находи — возвращает 0
            :return: key
        """
        return super().get(key, 0)


my_dict = MyDict({'one': 1, 'two': 2, 'three': 3, 'four': 4})
print('Key one:', my_dict.get('one'))
print('Key two:', my_dict.get('two'))
print('Key three:', my_dict.get('three'))
print('Key four:', my_dict.get('four'))
print('Key five:', my_dict.get('five'))
print('Key six:', my_dict.get('six'))