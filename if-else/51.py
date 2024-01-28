from math import sqrt
a = float(input('Введите значение а: '))
b = float(input('Введите значение b: '))
c = float(input('Введите значение c: '))

discriminant = b**2 - 4 * a * c

if discriminant < 0:
    print('Уравнение не имеет корней')
elif discriminant == 0:
    print(f'Уравнение имеет один действительный корень\nx1 = {(-b + sqrt(discriminant)) / (2 * a)}')  
elif discriminant > 0:
    print(f'Уравнение имеет два действительных корня\nx1 = {(-b + sqrt(discriminant)) / (2 * a)}\nx2 = {(-b - sqrt(discriminant)) / (2 * a)}')
