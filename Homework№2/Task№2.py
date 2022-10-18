# Задача №2: Написать программу, которая принимает на вход число N и выдает набор 
#            произведений чисел от 1 до N.

Factorial = int(input('N = '))
list=[]
a=1
for i in range(1,Factorial+1):
    a*=i
    list.append(a)
print(list)