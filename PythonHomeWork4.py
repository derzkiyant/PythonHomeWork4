from random import randint

"""
1. Пользователь вводит число, нужно вывести чило pi с заданной точностью(БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)
"""

print('\nРешение задачи 1:')

num_pi = 0

for i in range(1000):
    num_pi += 1/16**i * (4/(8*i+1) - 2/(8*i+4) - 1/(8*i+5) - 1/(8*i+6))

n = input('Задайте точность: ')

print(f'Вывод числа pi: {str(num_pi)[0:len(n)]}')


"""
2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

print('\nРешение задачи 2:')

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

print('\nРешение задачи 3:')

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

print('\nРешение задачи 4:')

k = int(input('Введите степень k: '))

f = ''

for i in range(k+1):
    if i == 0:
        f = str(randint(1, 100)) + f
    elif i == 1:
        f = str(randint(1, 100)) + '*' + 'x' + ' + ' + f
    else:
        f = str(randint(1, 100)) + '*' + 'x**' + str(i) + ' + ' + f

with open('file.txt', 'w+') as file:
    file.write(f'{f}' + ' = 0')

    file.seek(0, 0)
    for text in file:
        print(text)


"""
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
"""

print('\nРешение задачи 5:')

with open('file1.txt', 'r') as file1:
    text1 = file1.read().split(' = ')

with open('file2.txt', 'r') as file1:
    text2 = file1.read().split(' = ')

text1 = text1[0].split(' + ')
text2 = text2[0].split(' + ')

for i in range(len(text1)):
    if '*x' in text1[i]:
        text1[i] = text1[i].split('*x')

for j in range(len(text2)):
    if '*x' in text2[j]:
        text2[j] = text2[j].split('*x')

list4 = []
count = 0
for i in range(len(text1)):
    for j in range(count, len(text2)):
        if type(text1[i]) == list and type(text2[j]) == list:
            if len(text1[i][1]) == 3 and len(text2[j][1]) == 3:
                if int(text1[i][1][2]) > int(text2[j][1][2]):
                    count += 1
                    break
                elif int(text1[i][1][2]) == int(text2[j][1][2]):
                    text1[i][0] = str(int(text1[i][0]) + int(text2[j][0]))
                    list4.append(text1[i])
                else:
                    list4.append(text2[j])
                    count += 1
            elif len(text1[i][1]) != 3 and len(text2[j][1]) != 3:
                text1[i][0] = str(int(text1[i][0]) + int(text2[j][0]))
                list4.append(text1[i])
                break

        elif type(text1[i]) == str and type(text2[j]) == str:
            text1[i] = str(int(text1[i]) + int(text2[j]))
            list4.append(text1[i])

some_str = ''
for i in list4:
    if type(i) == list:
        some_str += i[0] + '*x' + i[1] + ' + '
    else:
        some_str += i

with open('file.txt', 'w+') as file:
    file.write(f'{some_str}' + ' = 0')

    file.seek(0, 0)
    for text in file:
        print(text)
