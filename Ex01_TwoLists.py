#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов 
# первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('Cколько элементов в первом списке: '))
first = []
for i in range(n):
    first.append(int(input('Введите элемент: ')))

m = int(input('Cколько элементов во втором множестве: '))
second = []
for i in range(m):
    second.append(int(input('Введите элемент: ')))

# Решение со встроенными функциями
# third = sorted(set(first + second))
# print(third) 


# Решение без встроенных функций
for i in first:
    if i not in second:
        second.append(i)


for i in range(len(second)):
    for j in range(1, len(second)):
        if second[j] < second[j-1]:
            temp = second[j]
            second[j] = second[j-1]
            second[j-1] = temp

print(second)

