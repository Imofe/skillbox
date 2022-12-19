class Property:
    """
    Базовый класс имущества.
    Args:
        worth(float): стоимость имущества
    """
    def __init__(self, worth):
        self.__worth = worth

    def get_worth(self):
        """
        Геттер для получения стоимости.
        :return: __worth
        :rtype: float
        """
        return self.__worth

    def get_tax(self):
        raise Exception('This method must be overriden')


class Apartment(Property):
    """
    Класс — квартира. Родитель: Property
    Args:
        worth: стоимость имущества
    Attributes:
        worth: стоимость имущества
        tax: налог на имущество
    """
    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        """
        Геттер для получения налога.
        :return: tax
        :rtype: float
        """
        return self.get_worth() / 1000


class Car(Property):
    """
    Класс машины. Родитель: Property
    Args:
        worth: стоимость машины
    Attributes:
        worth: стоимость машины
        tax: налог на машину
    """
    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        """
        Геттер для получения налога.
        :return: tax
        :rtype: float
        """
        return self.get_worth() / 200


class CountryHouse(Property):
    """
    Класс дача. Родитель: Property
    Args:
        worth: стоимость дачи
    Attributes:
        worth: стоимость дачи
        tax: налог на дачу
    """
    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        """
        Геттер для получения налога.
        :return: tax
        :rtype: float
        """
        return self.get_worth() / 500


while True:
    property_number = int(input('Выберите имущество:\n' + '1 - Квартира\n' + '2 - Автомобиль\n' + '3 - Дача\n' + '0 - Выход\n'))

    if property_number not in (0, 1, 2, 3):
        print('Введите корректное значение.')
        continue
    if property_number == 0:
        exit()
    money = float(input('Денег имеется: '))
    worth = float(input('Стоимость имущества: '))

    property = Apartment(worth) if property_number == 1 \
        else Car(worth) if property_number == 2  \
        else CountryHouse(worth)

    tax = property.get_tax()
    print(f'Налог на имущество: {tax}')
    money_left = 0 if money >= tax else property.get_tax() - money

    print(f'Необходимо денег: {money_left}\n')