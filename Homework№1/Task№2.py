# Задача №2: Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x = int(input('Enter X: '))
y = int(input('Enter Y: '))
if (x > 0 and y > 0):
    print('№ Quarter = 1')
if (x > 0 and y < 0):
    print("№ Quarter = 4")
if (x < 0 and y > 0):
    print('№ Quarter = 2')
if (x < 0 and y < 0):
    print("№ Quarter = 3")