coordinate = input("Введите координаты клетки: ")
letter = coordinate[0]
num = int(coordinate[1:])

if 1 <= num <= 8:
    if letter == 'a' and num % 2 == 0 or letter == 'c' and num % 2 == 0 or letter == 'e' and num % 2 == 0 or letter == 'g' and num % 2 == 0:
        print('Белая')
    elif letter == 'a' and num % 2 == 1 or letter == 'c' and num % 2 == 1 or letter == 'e' and num % 2 == 1 or letter == 'g' and num % 2 == 1:
        print('Черная')
    elif letter == 'b' and num % 2 == 0 or letter == 'd' and num % 2 == 0 or letter == 'f' and num % 2 == 0 or letter == 'h' and num % 2 == 0:
        print('Черная')
    elif letter == 'b' and num % 2 == 1 or letter == 'd' and num % 2 == 1 or letter == 'f' and num % 2 == 1 or letter == 'h' and num % 2 == 1:
        print('Белая')
    else:
        print('Неверная координата')
else:
    print('Число координаты больше допустимого')
