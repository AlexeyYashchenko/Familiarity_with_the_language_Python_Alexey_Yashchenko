#Задача№4: Напишите программу, которая принимает на вход координаты двух точек 
#          и находит расстояние между ними в 2D пространстве.
from math import sqrt
x1 = int(input('Enter X1 of point 1 = '))
y1 = int(input('Enter Y1 of point 1 = '))
x2 = int(input('Enter X2 of point 2 = '))
y2 = int(input('Enter Y2 of point 2 = '))

Distance=round(sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)),2)
print(f'Растояние между точками = {Distance}')