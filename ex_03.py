# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def transform(float_x):
    str_x = str(float_x)
    sum = 0
    for i in str_x:
        try:
            i = int(i)
            sum += i
        except:
            continue
    return sum
    
        


x = float(input('Число = '))

print(transform(x))