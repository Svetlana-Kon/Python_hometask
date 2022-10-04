# предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# -1-

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# БЫЛО:
# input_list = [int(input('Введите число: ')) for i in range(int(input('Введите количество элементов списка: ')))]
# mult_list = []
# for i in range (len(input_list) // 2 + len(input_list) % 2):
#     mult_list.append(input_list[i] * input_list[len(input_list) - 1 - i])
# print(mult_list)

# СТАЛО:
# input_list = [int(input('Введите число: ')) for i in range(int(input('Введите количество элементов списка: ')))]
# mult_list = []
# mult_list = [((input_list[i] * input_list[len(input_list) - 1 - i])) for i in range (len(input_list) // 2 + len(input_list) % 2)]
# print(mult_list)



# -2-

# Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

# my_list = [1, 5, 2, 3, 4, 6, 1, 7]
# res = [my_list[0]]
# [res.append(item) for item in my_list if item in my_list if item > res[-1]]
# print(res)




# -3-

# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

# БЫЛО
# user_list = [1, 2, 3, 5, 1, 5, 3, 10]
# result_list =[]
# for i in user_list:
#     if user_list.count(i) == 1:
#         result_list.append(i)
# print(result_list)


# СТАЛО
# user_list = [1, 2, 3, 5, 1, 5, 3, 10]
# result_list =[]
# result_list = [i for i in user_list if user_list.count(i) == 1]
# print(result_list)









