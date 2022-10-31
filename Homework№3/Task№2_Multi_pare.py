# Задача №2: Напишите программу, которая найдёт произведение пар чисел списка.
#            Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list_len = int(input('Enter lenght list = '))
list = []
for i in range(list_len):
    list.append(int(input(f'Enter number {i+1} = ')))
print(list)

list_multi = []
list_multi_len = int(len(list)/2+len(list)%2)

for i in range(list_multi_len):
    result = list[i]*list[len(list)-i-1]
    list_multi.append(result)
print(list_multi)