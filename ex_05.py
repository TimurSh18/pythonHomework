# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

def findNumber(x):
    number = [1, 9, 2, 5, 34, 19, 2, 10, 14]
    step = 1
    while step < len(number):
        if number[step] == x:
            print('Число найдено в списке чисел')
            print(number)
            break
        elif(step == len(number)-1 and number[step] != x):
            print('Число не найдено в списке чисел')
            print(number)
        step += 1    
            

x = int(input('Введите число, которое вы хотите найти: '))
findNumber(x)