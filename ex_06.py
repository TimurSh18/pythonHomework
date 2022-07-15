# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

def findStr(array, word):
    count = 0
    for i in range(len(array)):
        if array[i] == word:
            count += 1
        if(count == 2):
            return(f'Индекс второго вхождения в списке {i}')
    return('Второе вхождение отсутствует') 

word = input('Введите строку: ')

print(findStr(["qwe", "asd", "zxc", "qwe", "ertqwe"], word))