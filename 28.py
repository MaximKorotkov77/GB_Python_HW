# # Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# # *Пример:*

# # 2 2
# #     4 

a = int(input('введите a: '))
b = int(input('введите b: '))

def a_plus_b(a, b):
    if b < 1:
        return a      
    else:
        return    a_plus_b(a+1, b-1)

print(a_plus_b(a, b))