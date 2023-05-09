# Вычисляем длину гипотенузы
from math import sqrt

def hypotenuse_length(a, b):
    return sqrt(a**2 + b**2)

def main():
    x = int(input('Введите длину катета a: '))
    y = int(input('Введите длину катета b: '))
    print(f'Длина гипотенузы равна: {hypotenuse_length(x, y)}')
main()