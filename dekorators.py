from typing import Callable, Any


def do_twice(func: Callable) -> Callable:
    """Декоратор, исполняет декорируемую функцию дважды"""
    def wrapped_func(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        func(*args, **kwargs)
        return
    return wrapped_func


@do_twice                                                               # Декорирование функции в следующей строке
def greeting(name):
    print('Привет, {name}!'.format(name=name))
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