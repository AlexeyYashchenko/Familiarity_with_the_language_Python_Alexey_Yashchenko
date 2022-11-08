# Урок 4. Данные, функции и модули в Python. Продолжение
# Задача №1: Вычислить число c заданной точностью d

def pi(d=0.000001):
    s=0
    i=1
    sgn=1
    while True:
        a=4/i
        s=s+sgn*a
        if a<d:
            return s
        sgn=-sgn
        i=i+2
  
print(round(pi(),6))