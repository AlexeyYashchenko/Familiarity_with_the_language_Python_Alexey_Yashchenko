# Задача №3: Задайте список из n чисел последовательности (1+ 1\n)^n
#            и выведите на экран их сумму.

n = int(input('Enter follower from numbers n = '))
list = {}
sum = 0
for i in range(1, n+1):
    list[i] = round((1+1/i)**i, 2)
    sum+=list[i]
print(list)
print(round(sum,2))