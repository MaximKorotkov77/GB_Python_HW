# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint 

n = int(input('введите кол-во эл-тов N: '))


lst = []
for i in range(n):
        lst.append(randint(1,6))
print(lst)

x = int(input('введите искомое число Х: '))

print('-> ', lst.count(x))
        
