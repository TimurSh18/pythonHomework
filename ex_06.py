# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

def findStr(word):
    list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
    count = 0
    index = 0
    for i in list1:
        if i == word:
            count += 1
        if(count == 2):
            print(f'Индекс второго вхождения строки {word} = {index}')
            break
        if(index == len(list1)-1 and count != 2):
            print(f'Второго вхождения строки {word} в списке нет')
        index += 1  

word = input('Введите строку: ')
findStr(word)