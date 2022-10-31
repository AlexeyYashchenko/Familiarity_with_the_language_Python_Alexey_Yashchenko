#Задача №5: Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

lenght=int(input('Введите длину чисел Негафибоначчи: '))
negafibonnachi=[0]*(lenght*2+1)
negafibonnachi[lenght+1] = 1
negafibonnachi[lenght-1]= negafibonnachi[lenght+1]
for i in range(2,lenght+1):
    negafibonnachi[lenght+i] = negafibonnachi[lenght+i-2] + negafibonnachi[lenght+i-1]
    negafibonnachi[lenght-i] = negafibonnachi[lenght-i+2] - negafibonnachi[lenght-i+1]
print(f'Негафибоначчи числа {lenght}: {negafibonnachi}')