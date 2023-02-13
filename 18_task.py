
    # Задача 18: Требуется найти в массиве A[1..N] самый близкий по
    # величине элемент к заданному числу X. 
    # Пользователь в первой строке вводит натуральное число N – 
    # количество элементов в массиве. 
    # В последующих строках записаны N целых чисел Ai
    # Последняя строка содержит число X

from random import randint
n = int(input('Введите количество элементов в массиве: '))
lst = [randint(-1000, 1000) for i in range(n)]
print(lst)

x = int(input('Введите число Х: '))

if x > max((lst)):
    print(max(lst))
elif x < min(lst):
    print(min(lst))
else: 
    for i in sorted(lst):
        if i >= x:
            print(i)
            break