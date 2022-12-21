from random import randint

"""
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
"""

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

list4 = text1 + text2
list5 = []

for i in range(len(list4)):
    

for i in list4:
    if i[1] not in list5:
        if i[1] not in list4[list4.index(i)+1:]:
            list5.append(i)


print(list4)
print(list5)
