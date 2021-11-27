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
from typing import  Callable, Any, Optional
def repeats(_func: Optional[Callable] = None, *, num_of_repeat: int = 10) -> Callable:
    """Функция если принимает num_of_repeat то передает его декоратору.
        если num_of_repeat отсутсвует, срабатывает параметр num_of_repeat по умолчанию
    """
    def do_repeat(func: Callable) -> Callable:
        """Декоратор, исполняет декорируемую функцию дважды num_of_repeat раз"""
        def wrapped_func(*args, **kwargs) -> Any:
            for _ in range(num_of_repeat):
                func(*args, **kwargs)
            return
        return wrapped_func
    if _func is None:
        return do_repeat
    return do_repeat(_func)


@repeats(num_of_repeat=5)
def greeting(name):
    print('Привет, {name}!'.format(name=name))
greeting('Tom')

@repeats
def greeting_(name):
    print('Привет, {name}!'.format(name=name))
greeting_('Bob')
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
######################################################################################################################
import time
from datetime import datetime
from typing import Callable, Any
import functools

def create_time(cls: Callable) -> Callable:
    """Декоратор, выводит время создания инстанса класса"""
    @functools.wraps(cls)
    def wrapper(*args, **kwargs) -> Any:
        instance = cls(*args, **kwargs)
        print('\nВремя создания инстанса класса', datetime.utcnow())
        print('Методы сласса {}'.format(str(cls)[str(cls).rfind('.')+1:len(str(cls))-2]))
        for i_method in dir(cls):
            if i_method.startswith('__'):
                pass
            else:
                print('{}'.format(i_method), end=' ')
        return instance
    return wrapper


@create_time
class Square:
######################################################################################################################
import os
def for_all_methods(decorator: Callable) -> Callable:
    """
    Декоратор класса:
    Получает другой декоратор и применяет
     его ко все методам класса
    """

    @functools.wraps(decorator)
    def decorate(cls):
        print('for_all_methods')
        for i_method in dir(cls):
            if i_method.startswith('__'):
                pass
            else:
                cur_method = getattr(cls, i_method)
                decorator_method = decorator(cur_method)
                setattr(cls, i_method, decorator_method)
        return cls

    return decorate

def logging(func: Callable, *args, **kwargs) -> Any:
    """
    Декоратор записывает в файл log.txt дату время и результат
    выполнения метода
    """

    def wrapped_func(*args, **kwargs):
        # path = os.getcwd()
        # print(path)
        with open('/home/dyoma/ARB/Python/skillBox/Python_Basic/Lessons/task_29_4/log.txt', 'a',
                  encoding='utf8') as log_file:
            result = func(*args, **kwargs)
            log_file.write('{} {}\n'.format(datetime.utcnow(), result))
            return result  # результат работы функции func

    return wrapped_func

@for_all_methods(logging)
class Square:
    """
    Класс фигуры квадрат. Геттер и сеттер на длину стороны.
    Arg:
        length - длина стороны квадрата
    Arguments:
        __length - инкапсулированная длина стороны квадрата
    """

    def __init__(self, length: float) -> None:
        self.length = length

    @property
    def length(self) -> float:
        """Геттер длины стороны квадрата"""
        return self.__length

    @length.setter
    def length(self, new_length) -> None:
        """Сеттер длины стороны квадрата"""
        self.__length = new_length

    def square(self) -> float:
        """Возвращает площадь квадрата"""
        return self.length ** 2

    def perimeter(self) -> float:
        """Возвращает периметр квадрата"""
        return self.length * 4

path = os.getcwd()
print(path)

square_1 = Square(length=10)
square_2 = Square(length=5)
print(square_1.square())
print(square_2.square())
print(square_1.perimeter())
print(square_2.perimeter())