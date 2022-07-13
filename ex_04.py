# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def multiplication(steps):
    i = 1
    numbers = 1
    result = []
    while i <= steps:
        i += 1
        numbers = numbers*(i-1)
        result.append(numbers)
    return result    




N = int(input('Введите число до которого будут выданы произведения: '))

print(multiplication(N))