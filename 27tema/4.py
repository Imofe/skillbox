from collections.abc import Callable
import functools


def counter(func: Callable) -> Callable:
    """
    Декоратор. Считают количество вызовов функции и выводит в консоль
    :param func: Декорируемая функция
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        wrapped.count += 1
        result = func(*args, **kwargs)
        print(f'Функция {func.__name__} вызывалась {wrapped.count} раз')
        return result

    wrapped.count = 0
    return wrapped

@counter
def test():
    print('Загрузка...')


test()
test()
test()
