# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


num = int(input('введите трехзначное число: '))
first = num // 100
second = num%100 // 10
fird = num%10
s = first + second + fird

print(num, '->', s, '(', first, '+', second, '+', fird, ')')