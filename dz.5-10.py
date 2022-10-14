# Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список 
# и выведите их в порядке возрастания.
# Примечание. И даже эту задачу на Питоне можно решить в одну строчку.


# print(*sorted(set(input('Введите список чисел: ').split()).intersection(set(input('Введите еще один список чисел: ').split())), key=int))




# Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите 
# слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, 
# если не встречалось


# numbers = [int(number) for number in input().split()]
# met_before = set()
# for num in numbers:
#     if num in met_before:
#         print('YES')
#     else:
#         print('NO')
#         met_before.add(num)





# Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько 
# различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним 
# или большим числом пробелов или символами конца строки.
# Sample Input:
# 4
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.
# Sample Output:
# 19

# num_strings = int(input('Введите число строк: '))

# some_list = []
# for i in range(num_strings):
#     for some_word in input('Введите строку из слов: ').split():
#         some_list.append(some_word)
        
# print(len(set(some_list)))


