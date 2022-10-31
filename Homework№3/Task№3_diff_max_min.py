# Задача №3: Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
#            максимальным и минимальным значением дробной части элементов.

list_len = int(input('Введите длину списка = '))
list = []
for i in range(list_len):
    list.append(float(input(f'Enter number {i+1} = ')))
# print(list)

min=1
max=0
for i in list:
    if(i-int(i)) <= min:
        min=i-int(i)       
    if(i-int(i)) >= max:
        max=i-int(i)
diff = round(max-min,8)

print(f'Разница между максимальным и минимальным значением дробной части элементов, списка {list} => {diff}')