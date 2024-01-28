from math import cos, sin, radians, acos


t1 = float(input("Введите координаты широты 1 точки: "))
g1 = float(input("Введите координаты долготы 1 точки: "))
t2 = float(input("Введите координаты широты 2 точки: "))
g2 = float(input("Введите координаты долготы 2 точки: "))
distance = 6371.01 * acos(sin(radians(t1)) * sin(radians(t2)) + cos(radians(t1)) * cos(radians(t2)) * cos(radians(g1 - g2)))
print(f'Расстояние между точками равно: {distance}')
