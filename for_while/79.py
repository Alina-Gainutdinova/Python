n = int(input("Введите положительное число: "))
m = int(input("Введите следующее положительное число: "))

d = min(n, m)

while n % d != 0 or m % d != 0:
    d = d - 1
print(f'Наибольший общий делитель равен {d}')    