# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите кол-во эл-тов набора 1: '))
m = int(input('Введите кол-во эл-тов массива 2: '))

lst_n = list()
lst_m = list()
print('Введите эл-ты набора 1:')
for i in range(n):
    lst_n.append(int(input()))

print('Введите эл-ты набора 2:')
for i in range(m):
    lst_m.append(int(input()))

print(lst_n)

lst_mn = list()
for i in range(n):
    if lst_n[i] in lst_m and lst_n[i] not in lst_mn:
        lst_mn.append(lst_n[i])

for i in range(len(lst_mn)):
    for j in range((len(lst_mn)-1)):
        if lst_mn[j]>lst_mn[j+1]:
            change = lst_mn[j]
            lst_mn[j] = lst_mn[j+1]
            lst_mn[j+1] = change
         
print(lst_mn)

