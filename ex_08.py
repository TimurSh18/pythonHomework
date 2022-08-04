# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов.

first = open("first.txt", "r")
first_sp = first.read().split(' + ')

second = open("second.txt", "r")
second_sp = second.read().split(' + ')
newfirst = []
newsecond = []

for i in first_sp:
    newfirst.append(i.split('x^'))

for i in second_sp:
    newsecond.append(i.split('x^'))

print(newfirst) 
print(newsecond)

result = []
for i in newfirst:
    for j in newsecond:
        if len(i) > 1:
            if len(j) > 1:
                if i[-1] == j[-1]:
                    result.append(f"{int(i[0]) + int(j[0])}x^{int(i[-1])}")
                    result.append(f"+")
        if len(i) == 1:
            if len(j) == 1:
                result.append(f"{int(i[0]) + int(j[0])}")
            
 
print(result)
str_result = ' '.join(result)

hello = open("result.txt", "a")
hello.write(f'{str_result}\n')
hello.close()

first.close()
second.close()