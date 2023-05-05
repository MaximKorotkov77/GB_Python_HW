# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint 

n = int(input('Введите кол-во эл-тов массива: '))

lst_n = list()
for i in range(n):
    lst_n.append(randint(0,10))
print(lst_n)
 
a = int(input('Введите нижнюю границу диапазона a: '))
b = int(input('Введите верхнюю границу диапазона b: '))

def lst_ind(a, b):
    lst_in = list()
    for i in range(n):
        if lst_n[i] in range(a-1, b+1):
            lst_in.append(i)
    return lst_in

print(lst_ind(a, b))