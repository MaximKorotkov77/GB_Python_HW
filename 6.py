# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

num = int(input('введите номер билета: '))

d_4 = num%1000 // 100
d_5 = num%100 // 10
d_6 = num%10
s_4_6 = d_4 + d_5 + d_6

d_3 = num%10000 // 1000
d_2 = num%100000 // 10000
d_1 = num // 100000
s_1_3 = d_1 + d_2 + d_3

if s_4_6 == s_1_3 :
    print(num, '->', 'yes')
else:
    print(num, '->', 'no')
