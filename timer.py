import time
from typing import Callable, Any


def timer(func: Callable, *args, **kwargs) -> Any:
    """Функция таймер. Выводит время работы функции и возвращает ее результат"""
    started_at = time.time()
    result = func(*args, **kwargs)
    ended_at = time.time()
    run_time = round(ended_at - started_at, 3)
    print('Время работы функции {} сек.'.format(run_time))
    return result                                                           # результат работы функции func


def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([num ** 3 for num in range(100000)])
    return result


my_result = timer(cubes_sum, 100)
print(my_result)

########################################################################################################################
from _collections_abc import Iterator
from contextlib import contextmanager


@contextmanager
def timer() -> Iterator:
    """Функция контекст менеджер. Считает время выполнения кода"""
    start = time.time()
    try:
        yield
    finally:
        print('timer = ', time.time() - start)


with timer() as t1:
    print('Первая часть')
    val_1 = 100 * 100 ** 1000000
    # какой то код