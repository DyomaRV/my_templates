import functools
from typing import Callable, Any



def do_twice(func: Callable) -> Callable:
    """Декоратор, исполняет декорируемую функцию дважды"""
    @functools.wraps(func)                                             # присваеваем обертке методы обертываемой функции
    def wrapped_func(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        func(*args, **kwargs)
        return
    return wrapped_func


@do_twice                                                               # Декорирование функции в следующей строке
def greeting(name):
    '''функция выводящяя 'Привет' '''
    print('Привет, {name}!'.format(name=name))

print(greeting.__name__)                                                # без @functools.wraps(func) в декораторе не
print(greeting.__doc__)                                                 #  работает выведет значения для def wrapped_func
######################################################################################################################


def timer(func: Callable, *args, **kwargs) -> Any:
    """Декоратор таймер. Выводит время работы функции и возвращает ее результат"""
    def wrapped_func(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 3)
        print('Время работы функции {} сек.'.format(run_time))
        return result                                                           # результат работы функции func
    return wrapped_func

@timer
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([num ** 3 for num in range(10000)])
    return result


my_result = cubes_sum(100)
print(my_result)
######################################################################################################################
def decor_timesleep(func: Callable) -> Callable:
    """Декоратор, задержка перед выводом функции на x секунд"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        time.sleep(3)
        func(*args, **kwargs)
        return
    return wrapped_func

######################################################################################################################
import functools
from typing import Callable, Any
import time
from datetime import datetime, date, time


def logging(func: Callable) -> Callable:
    """Декоратор, ловит ошибки при работе функций и записывает их в файл"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print('\nfunc name: {}\n{}'.format(func.__name__, func.__doc__))
        try:
            func(*args, **kwargs)
        except BaseException as exception:
            with open('function_errors.log', 'a', encoding='utf8') as log_file:
                log_file.write('{} func: {} {} ({})\n'.format(
                    datetime.now(),
                    func.__name__,
                    exception.__class__.__name__,
                    exception.__str__()
                ))
        return
    return wrapped_func

import functools
from typing import Callable, Any
######################################################################################################################
def counter(func: Callable) -> Callable:
    """Декоратор, считающий и выводящий количество вызовов декорируемой функции."""

    @functools.wraps(func)
    def wrapped_func(counter_dict=dict(), *args, **kwargs) -> Any:
        if func.__name__ not in counter_dict.keys():
            counter_dict.update({func.__name__: 1})
        else:
            counter_dict[func.__name__] += 1
        print('{}-й вызов функции {}'.format(
            counter_dict[func.__name__],
            func.__name__
        ))
        result = func(*args, **kwargs)
        return result
    return wrapped_func