import random


class KillError(Exception):
    """
    Класс: убийство. Родитель: Exception
    """
    pass


class DrunkError(Exception):
    """
    Класс: пьянство. Родитель: Exception
    """
    pass


class CarCrashError(Exception):
    """
    Класс: попадание в аварию. Родитель: Exception
    """
    pass


class GluttonyError(Exception):
    """
    Класс: обжорство. Родитель: Exception
    """
    pass


class DepressionError(Exception):
    """
    Класс ошибки депрессии. Родитель: Exception
    """
    pass


class Buddhist:
    """
    Класс: буддист.
    Args:
        karma - Начальная карма (изначально 0)
    """
    def __init__(self, karma=0):
        self.__karma = karma

    def get_karma(self):
        """
        Геттер для получения кармы.
        :return: karma
        :rtype: int
        """
        return self.__karma

    def set_karma(self, karma):
        """
        Сеттер для добавления очков кармы.
        :rtype: int
        """
        self.__karma += karma


def one_day():
    if random.randint(1, 10) == 1:
        raise random.choice([DrunkError('Напился'),
                             KillError('Убил'),
                             GluttonyError('Обжорство'),
                             CarCrashError('Попал в аварию'),
                             DepressionError('Депрессия')])

    return random.randint(1, 7)


with open('karma.log', 'w', encoding='utf8') as karma_log:
    karma_log.close()

MAX_KARMA = 500
buddhist = Buddhist()
day = 0

while buddhist.get_karma() < MAX_KARMA:
    day += 1
    try:
        buddhist.set_karma(one_day())
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as err:
        with open('karma.log', 'a', encoding='utf8') as karma_log:
            err_message = f'{err.__class__.__name__}. {err}'
            karma_log.write(f'День {day}. {err_message}\n')
else:
    print('Достигнут максимум кармы!')