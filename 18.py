from math import pi

r = float(input("Введите радиус цилиндра: "))
h = float(input("Введите высоту цилиндра: "))
s = pi * r**2
v = s * h
print(f'Обьем цилиндра равен: {v:.1f}')
