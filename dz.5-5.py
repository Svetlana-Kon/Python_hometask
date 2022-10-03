# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# my_str = 'Мы неабв очень любим Питон иабв Джавуабв!'.split()
# print(' '.join([word for word in my_str if 'абв' not in word]))




# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять 
# первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""



# ДВА ИГРОКА


# import random

# rules = ('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. '
#     'Первый ход определяется жеребьёвкой.'
#     'За один ход можно забрать не более чем 28 конфет. '
#     'Все конфеты оппонента достаются сделавшему последний ход. '
#     'Сколько конфет нужно взять первому игроку, '
#     'чтобы забрать все конфеты у своего конкурента?')
            
# print(rules)

# player1 = input('\nИмя первого игрока: ')
# player2 = input('\nИмя второго игрока: ')
# players = [player1, player2]

# amount = 2021
# max_move = 28
# print(f'Первому игроку нужно взять {amount%(max_move + 1)} конфет, чтобы выиграть \n')

# def play_game(n, m, players):
#     count = random.randint(0, 1)
#     while n > 0:
#         print(f'{players[count%2]}, возьмите конфеты')
#         move = int(input())
#         while move > n or move > m or move == 0:
#             print(f'Нужно взять от одной до {m} конфет, сейчас у нас всего {n}')
#             move = int(input())
#         n = n - move
#         if n > 0: print(f'Осталось конфет: {n}')
#         else: print('Все конфеты разобраны.')
#         count +=1
#     return players[not count%2]

# winer = play_game(amount, max_move, players)
# if not winer:
#     print('У нас нет победителя.')
# else: print(f'Победитель {winer}!')



# ИГРА С "ГЛУПЫМ" БОТОМ

# import random

# rules = ('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. '
#     'Первый ход определяется жеребьёвкой.'
#     'За один ход можно забрать не более чем 28 конфет. '
#     'Все конфеты оппонента достаются сделавшему последний ход. '
#     'Сколько конфет нужно взять первому игроку, '
#     'чтобы забрать все конфеты у своего конкурента?')
            
# print(rules)

# player1 = input('\nИмя первого игрока: ')
# bot_name = 'Bot_player '
# print(f'\nВторой игрок: {bot_name}\n')
# players = [player1, bot_name]

# amount = 100
# max_move = 28
# print(f'Первому игроку нужно взять {amount%(max_move + 1)} конфет, чтобы выиграть \n')

# def play_game(n, m, players):
#     count = random.randint(0, 1)
#     print(f'{count+1}!: первым берет конфеты {players[count]} \n')
#     while n > 0:
#         print(f'{players[count%2]}, возьмите конфеты')
#         if players[count%2] != bot_name:
#             move = int(input())
#         else: 
#             move = random.randint(1, m)
#             print(f'Bot_player move = {move}')
#         while move > n or move > m or move == 0:
#             print(f'Нужно взять от одной до {m} конфет, сейчас у нас всего {n}')
#             if players[count%2] != bot_name:
#                 move = int(input())
#             else: 
#                 move = random.randint(1, n)
#                 print(f'Bot_player move = {move}')
#         n = n - move
#         if n > 0: print(f'Осталось конфет: {n}')
#         else: print('Все конфеты разобраны.')
#         count +=1
#     return players[not count%2]

# winer = play_game(amount, max_move, players)
# if not winer:
#     print('У нас нет победителя.')
# else: print(f'Победитель {winer}!')





# Создайте программу для игры в "Крестики-нолики".

# cell_number = ('\nНумерация ячеек на игровом поле: \n\n'
#     '|02|12|22|\n'
#     '----------\n'
#     '|01|11|21|\n'
#     '----------\n'
#     '|00|10|20|\n')
            
# print(cell_number)

# board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

# winner = None
# full = False
# moves = []
# game = True 

# def display():
#     for i in board:
#         print("-"*7)
#         for j in i:
#             print("|"+j, end= "")
#         print("|")
#     print("-"*7)

# def win(player):
#     global winner
#     b = board
#     hori = b[0][0]==b[0][1]==b[0][2]!= ' ' or b[1][0]==b[1][1]==b[1][2]!=' ' or b[2][0]==b[2][1]==b[2][2]!= ' '
#     verti = b[0][0]==b[1][0]==b[2][0]!= ' ' or b[0][1]==b[1][1]==b[2][1]!= ' ' or b[0][2]==b[1][2]==b[2][2]!= ' '
#     dia = b[0][0]==b[1][1]==b[2][2]!= ' ' or b[2][0]==b[1][1]==b[0][2]!= ' ' 
#     if hori or verti or dia:
#         winner = player
#     for i in board:
#         if " " in i:
#             full = False
#             break
#         else:
#             full = True
#     if full and not winner:
#          winner = 'draw'

   
# player = 'X'
# while game:
#     move = input(f"В какую ячейку поставим ({player})? ")
#     if move not in moves:
#         moves.append(move)
#     else:
#         print("Эта ячейка занята!")
#         continue
#     try:
#         x,y = int(move[0]), int(move[1])
#     except:
#         print("Будьте внимательны при указании адреса ячейки")
#         continue
#     board[2-y][x] = f"{player}"

#     display()
#     win(player)
#     if winner == player:
#         print(f"{player} победитель!")
#         game = False
#     elif winner == 'draw':
#         print('Ничья!')
#         game = False
#     if player =='X':
#         player = 'O'
#     else:
#         player = 'X'








# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# with open('5-5_decoded.txt', 'r') as data:
#     some_text = data.read()

# def encode_rle(some_symb):
#     str_code = ''
#     prev_char = ''
#     count = 1
#     for char in some_symb:
#         if char != prev_char:
#             if prev_char:
#                 str_code += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     return str_code

            
# str_code = encode_rle(some_text)
# print(str_code)

# with open('5-5_encoded.txt', 'r') as data:
#     some_text2 = data.read()

# def decoding_rle(some_symb:str):
#     count = ''
#     str_decode = ''
#     for char in some_symb:
#         if char.isdigit():
#             count += char 
#         else:
#             str_decode += char * int(count)
#             count = ''
#     return str_decode

# str_decode = decoding_rle(some_text2)
# print(str_decode)


