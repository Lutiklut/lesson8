
#3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.

#4. Сравнить объем оперативной памяти для функции создания генератора и функции создания списка с элементами: натуральные числа от 1 до 1000000.

import time
import requests
import os
import psutil




def show_decor(f):

    def wrapper(*args, **kwargs):

        proc = psutil.Process(os.getpid())
        print('Исп. память до вып. функции:' + str(proc.memory_info().rss/1000000))
        print(f(*args,**kwargs))
        proc1 = psutil.Process(os.getpid())
        print('Исп. память после вып. функции:' + str(proc1.memory_info().rss / 1000000))
        proc_simple = int(proc1.memory_info().rss / 1000000) - (proc.memory_info().rss / 1000000)
        print('Использованная память:' + str(proc_simple))

    return wrapper

@show_decor
def func_for_decor(n):
    new_list = []
    for i in range(1, n + 1):
        new_list.append(i)
    return new_list

list_ex = func_for_decor(1000)





@show_decor
def nums(num):

    for i in range(1,num+1):
        yield i




nums_ex=nums(1000)

#Не получилось. не понимаю,почему разность отрицательная и почему для генератора разность такая же,
# как и для обычной функции, хотязначения вроде другие