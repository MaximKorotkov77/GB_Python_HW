
# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input('введите A: '))
b = int(input('введите B: '))

def a_in_b(a, b):
    if b == 1 :
        return a
    else:
        return a_in_b(a, b-1) * a_in_b(a, 1)
       
print(a_in_b(a, b))

    