from math import sqrt


s1 = float(input("Введите первую длину стороны треугольника: "))
s2 = float(input("Введите вторую длину стороны треугольника: "))
s3 = float(input("Введите третью длину стороны треугольника: "))
s = (s1 + s2 + s3) / 2
area = sqrt(s * (s-s1) * (s-s2) * (s-s3))
print(f'Площадь треугольника равна: {area}')
