# медиана трех значений 
import math
# #def median(a,b,c):
#     a = int(input('Введите 1-ую сторону: '))
#     b = int(input('Введите 2-ую сторону: '))
#     c = int(input('Введите 3-ую сторону: '))
#     m = a + b + c - min(a,b,c) + max(a,b,c)
#     print(f'Медиана 3-х чисел равна: {m}')
# median()

def median(a, b, c):
    if a < b and b < c or a > b and b > c:
        return b
    if b < a and a < c or b > a and a > c:
        return a
    if c < a and b < c or c > a and b > c:
        return c

def alternateMedian(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)
# Выводим медиану чисел, введенных пользователем
def main():
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    z = float(input("Введите третье число: "))
    print("Медиана равна:", median(x, y, z))
    print("С помощью альтернативного метода:", \
    alternateMedian(x, y, z))
    # Вызываем основную функцию
main()