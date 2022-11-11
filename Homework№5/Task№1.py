# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
# Задача №1: Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'абвгдейка интересно абвыралг клон бравоабв'
list = text.split(' ')
print(list)

find ='абв'
list = [i for i in text.split() if find not in i]
print(f'Result: {" ".join(list)}')