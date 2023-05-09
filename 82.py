num = int(input('Введите целое число: '))

result = ""
q = num

while q > 0:
    r = q % 2
    result = str(r) + result
    q = q // 2
print(f'Число в двоичной системе счисления: {result}')