n = int(input('Введите целое число (2 или больше): '))
print(f'Простые множители числа {n}: ')

factor = 2 
if n > 1:
    while factor <= n:
        while n % factor == 0:
            print(factor)
            n //= factor
        factor += 1     
else:
    print('Ошибка!(число меньше двух)')
       
      