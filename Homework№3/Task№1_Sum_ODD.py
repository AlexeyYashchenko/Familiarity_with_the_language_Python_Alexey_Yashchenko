# Задача №1: Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#            стоящих на нечётной позиции.

import random
N = 7
list = []
for i in range(N):
    list.append(random.randint(-10, 10))
print(list)

sum = 0
for i in range(len(list)):
    if i % 2 == 1:
        sum += list[i]
print(f'Сумма эл-тов стоящих на нечетных позициях = {sum}')
