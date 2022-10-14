#Задача №1: Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
#           и проверяет, является ли этот день выходным.
day = int(input('Enter a number for the day of the week = '))
if 1 > day or day > 7:
    print('No such day of the week')
if 0 < day < 6:
    print('This day isn`t a day off')
if day == 6 or day == 7:
    print('This day a day off')