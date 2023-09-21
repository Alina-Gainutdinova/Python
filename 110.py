data = []

num = int(input("Введите целое число (0 для окончания ввода): "))

while num != 0:
    data.append(num)
    num = int(input("Введите целое число (0 для окончания ввода): "))

data.sort()


for i in data:
    print(i)