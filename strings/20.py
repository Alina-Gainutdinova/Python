p = float(input("Введите давление в Паскалях: "))
v = float(input("Введите объём в литрах: "))
t = float(input("Введите температуру в градусах Цельсия: "))
r = 8.314 #Универсальная газовая постоянная Дж/(моль*К)
t1 = t + 273.15
n = (p * v) / (r * t1)
print(f'Количество газа равно: {n} моль')

