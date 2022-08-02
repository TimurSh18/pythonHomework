# Написать список простых множителей, заданного числа

def findList(n):
    list_mn = []
    for i in range(2,n):
        if n % i == 0:
            list_mn.append(i)
    return(list_mn)




x = int(input('Введите число: '))
print(findList(x))