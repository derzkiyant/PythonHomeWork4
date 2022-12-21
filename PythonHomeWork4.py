from random import randint

"""
1. Пользователь вводит число, нужно вывести чило pi с заданной точностью(БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)
"""

# num_pi = 0

for i in range(1000):
    num_pi += 1/16**i * (4/(8*i+1) - 2/(8*i+4) - 1/(8*i+5) - 1/(8*i+6))

n = input('Задайте точность: ')

print(f'Вывод числа pi: {str(num_pi)[0:len(n)]}')


"""
2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

n = int(input('Введите число N: '))
list1 = []

for i in range(1, n + 1):
    if n % i == 0:
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            list1.append(i)
print(list1)


"""
3. Задайте последовательность чисел. Напишите программу, которая выведет
список неповторяющихся элементов исходной последовательности.
"""

list2 = [randint(0, 10) for _ in range(int(input('Введите размер списка: ')))]
list3 = []

print(f'Начальный список: {list2}')

for i in list2:
    if i not in list3:
        if i not in list2[list2.index(i)+1:]:
            list3.append(i)

print(f'Итоговый список: {list3}')


"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
*Пример:* 
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""

k = int(input('Введите степень k: '))

f = ''

for i in range(k+1):
    if i == 0:
        f = str(randint(1, 100)) + f
    elif i == 1:
        f = str(randint(1, 100)) + '*' + 'x' + ' + ' + f
    else:
        f = str(randint(1, 100)) + '*' + 'x**' + str(i) + ' + ' + f

with open('file2.txt', 'w+') as file:
    file.write(f'{f}' + ' = 0')

    file.seek(0, 0)
    for text in file:
        print(text)
