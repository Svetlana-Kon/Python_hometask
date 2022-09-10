# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input('Введите число: ')
# sum = 0
# for i in number:
#     if i != '.' and i != ',':
#         sum += int(i)
# print(sum)




# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел 
# от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите число: '))
# list_pr = []
# pr = 1
# for i in range (1, n+1):
#     list_pr.append(pr*i)
#     pr *= i
# print(list_pr)





# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input('Введите число: '))
# sum = 0
# for i in range (1, n+1):
#     sum += (1 + 1/i)**i
# print(sum)





# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.

# from random import *
# n = int(input('Введите число: '))

# list = [randint(-n, n) for i in range(n)]
# print(list)

# pos = open('positions.txt', 'w')
# for i in range(randint(2, len(list))):
#     pos.write(str(randint(0, len(list)-1)) + '\n')
# pos.close

# pr = 1
# with open('positions.txt', 'r') as pos:
#     for i in pos.read().splitlines():
#         pr = pr * list[int(i)]
# print(pr)




# Реализуйте алгоритм перемешивания списка.

# list = [':-)', 12, 4.52, 'hello', 'привет']
# print(list)
# import random
# random.shuffle(list)
# print(list)


