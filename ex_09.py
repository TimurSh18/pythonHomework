# Дан список чисел. 
# Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.

def buildList(y):
    spisok = []
    step = 1
    spisok.append(step)
    index = 0
    while index < len(y):
        if y[index] == step + 1:
            spisok.append(y[index])
            index = 0
            step += 1
            if index == len(y) -1:
                break
        index += 1
    return spisok

def findNeed(spisok):
    last_list = []
    min = spisok[0]
    last_list.append(min)
    max = spisok[0]
    for i in spisok:
        if i > max and i == spisok[len(spisok)-1]:
            max = i
            last_list.append(max)
    return last_list

start = [1, 5, 2, 3, 4, 1, 7]
print(findNeed(buildList(start)))       