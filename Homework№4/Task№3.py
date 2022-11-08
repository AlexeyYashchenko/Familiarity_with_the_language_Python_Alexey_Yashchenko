
# Задача№ 3. Задайте последовательность чисел. Написать программу, которая выведет список 
#            неповторяющихся элементов исходной последовательности.
subsequence = input('Sequence: ').split()
array=[]
for i in subsequence:
    if i not in array:
        array.append(i)
print(array)