# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint 

n = int(input('введите кол-во эл-тов N: '))

lst = []
for i in range(n):
        lst.append(randint(1,6))
print(lst)

x = int(input('введите число Х: '))
dif = max(lst)
find_next = lst[0]
for i in lst:
        if abs(i - x) < dif:
                dif = abs(i - x)
                find_next = i

print(find_next)   