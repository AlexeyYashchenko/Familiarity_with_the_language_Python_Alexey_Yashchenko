# Задача№ 2: Задайте натуральное число N. Напишите программу, которая составит список 
#            простых множителей числа N.
N = int(input("Enter number: "))
i = 2 
list = []
N1 = N
while i <= N:
    if N % i == 0:
        list.append(i)
        N //= i
        # i = 2
    else:
        i += 1
print(f"Prime factors of a number {N1} in list: {list}")
