#Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def checkCoordinates(x, y):
    if(x > 0 and y > 0):
        print('Точка находится в I четверти')
    elif(x > 0 and y < 0):
        print('Точка находится в IV четверти')
    elif(x < 0 and y > 0):
        print('Точка находится в II четверти')
    elif(x < 0 and y < 0):
        print('Точка находится в III четверти')
    elif(x == 0 and y != 0 ):
        print('Точка лежит на оси координат Oy')
    elif(x != 0 and y == 0):
        print('Точка лежит на оси координат Ox')
    elif(x == 0 and y == 0):
        print('Точка лежит в начале координат!')

x = int(input('Координата x = '))
y = int(input('Координата y = '))

checkCoordinates(x, y)