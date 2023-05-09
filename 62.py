from random import randrange

red = 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34
green = 0, 37
black = 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35, 36

value = randrange(0, 38)

if value == 37:
    print(f'Выпавший номер: 00')
else:
    print(f'Выпавший номер: {value}')

if value == 37:
    print(f'Выигравшая ставка: 00')    
else:
    pass

if value in red:
    print('Выигравшая ставка: красное')
elif value in green:
    pass
else:
    print('Выигравшая ставка: черное')

if value >= 1 and value <= 36:
    if value % 2 == 1:
        print("Выигравшая ставка: нечетное")
    else:
        print("Выигравшая ставка: четное")

if value >= 1 and value <= 18:
    print("Выигравшая ставка: от 1 до 18")
elif value >= 19 and value <= 36:
    print("Выигравшая ставка: от 19 до 36")
