a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
min_num = min(a, b, c)
max_num = max(a, b, c)
middle_num = (a + b + c) - (min_num + max_num)
print(f'{min_num}, {middle_num}, {max_num}')