# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi

# count = 0
# for i in range(len(input('input d: ').split('.')[1])):
#     count += 1

# print(round(pi, count))





# Задайте натуральное число N. Напишите программу, которая составит список простых 
# множителей числа N.


# number = int(input("Введите натуральное число: "))

# list_mult= []
# for i in range(2, number+1):
#     while number%i == 0:
#         list_mult.append(i)
#         number = number/i
   
# print(list_mult)






# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

# user_list = [1, 2, 3, 5, 1, 5, 3, 10]

# result_list =[]
# for i in user_list:
#     if user_list.count(i) == 1:
#         result_list.append(i)

# print(result_list)





# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = 3

import random

coefficient = [random.randint(1, 100)]

for i in range (0, k):
    coef = random.randint(0, 10) 
    coefficient.append(coef)
print(coefficient)

for i in range(0, k-1):
    if coefficient[i] != 0:
        data = open('polyndrom_k.txt', 'a')
        data.writelines(f'{coefficient[i]}*x^{k-i}+')
        data.close()

for i in range(k-1, k):
    if coefficient[i] != 0:
        data = open('polyndrom_k.txt', 'a')
        data.writelines(f'{coefficient[i]}*x')
        data.close()


data = open('polyndrom_k.txt', 'a')
if coefficient[k] != 0:
    data.writelines(f'+{coefficient[-1]}=0')
else:
    data.writelines('=0')
data.write('\n')
data.close()






# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать 
# файл, содержащий сумму многочленов.


# не смогла решить :(((