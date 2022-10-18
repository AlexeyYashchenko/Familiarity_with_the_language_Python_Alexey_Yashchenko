# Урок 2. Знакомство с Python. Продолжение
# Задача №1: Написать программу, которая принимает на вход вещественное число и показывает сумму 
#            его цифр
#  Пример:   6782 -> 23;  0,56 -> 11

rn = input('Enter real number : ')
rn=rn.replace('.','')
rn=rn.replace(',','')
a=list(rn)

sum=0
for i in a:
    sum+=int(i)
print(sum)