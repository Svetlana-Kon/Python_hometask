# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# input_list = [int(input('Введите число: ')) for i in range(int(input('Введите количество элементов списка: ')))]

# sum = 0
# for i in range(1, len(input_list), 2):
#     sum += input_list[i]
# print(sum)




# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# input_list = [int(input('Введите число: ')) for i in range(int(input('Введите количество элементов списка: ')))]

# mult_list = []
# for i in range (len(input_list) // 2 + len(input_list) % 2):
#     mult_list.append(input_list[i] * input_list[len(input_list) - 1 - i])
# print(mult_list)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу м
# ежду максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# a = [float(input('Введите число: ')) for i in range(int(input('Введите количество элементов списка: ')))]

# input_list = [float('0.' + str(i).split('.')[1]) for i in a if '.' in str(i)]
# print(max(input_list) - min(input_list))




# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input('Введите число: '))

# binary_string = ''
# while n > 0:
#     binary_string = str(n % 2) + binary_string
#     n //= 2
# print(binary_string)




# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число: '))

fibon_list = [0]*(k*2 + 1)
fibon_list[k] = 0
fibon_list[k+1] = 1

for i in range(k + 2, len(fibon_list)):
    fibon_list[i] = fibon_list[i-2] + fibon_list[i-1]

for i in range(k, -1, -1):
    if i%2 == 0:
        fibon_list[i] = fibon_list[k*2-i]*(-1)
    else:
        fibon_list[i] = fibon_list[k*2-i]




print(fibon_list)





