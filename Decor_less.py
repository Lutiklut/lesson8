
#1. Написать декоратор, замеряющий время выполнение декорируемой функции.

import time
import requests

def show_time(f):

    def wrapper(*args, **kwargs):
        print(time.time())
        print(f(*args,**kwargs))
        print(time.time())
    return wrapper

@show_time
def func_for_decor(n):
    new_list = []
    for i in range(1, n + 1):
        new_list.append(i)
    return new_list



list_ex = func_for_decor(1000)

