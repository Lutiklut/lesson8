import sys
import time
import clock
#Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).
import random


N=10000000
list_nat=(x for x in range(1, N+1))
print (list_nat)

def simple_create (n):

    new_list=[]
    for i in range(1,n+1):
        new_list.append(i)

    return new_list

start=time.time()
new_list=simple_create(N)
stop=time.time()

print(new_list)
print("заняло {} секунд".format(stop-start))

def nums(num):

    for i in range(1,num+1):
        yield i


start = time.time()
nums_ex=nums(N)
stop=time.time()
print("У генератора заняло {} секунд".format(stop-start))
print(nums_ex)
