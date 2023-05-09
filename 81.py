binary = input("Введите число в двоичной системе: ")
decimal = 0
x = len(binary) - 1
for i in binary:
    decimal += int(i) * (2 ** x)
    x -= 1
print(f'Число в десятичной системе: {decimal}')

# 111 = 7
# 0 + 1 * 2**2 = 4; x = 1
# 4 + 1 * 2**1 = 6; x = 0
# 6 + 1 * 2**0 = 7 