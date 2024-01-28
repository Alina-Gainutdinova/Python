month = input('Введите месяц: ')
day = int(input('Введите номер дня: '))

if 0 <= day <= 31:

    if day >= 20 and month == 'Март' or month == 'Апрель' or month == 'Май' or day < 21 and month == 'Июнь':
        print('Весна')
    elif day >= 21 and month == 'Июнь' or month == 'Июль' or month == 'Август' or day < 22 and month == 'Сентябрь':
        print('Лето')
    elif day >= 22 and month == 'Сентябрь' or month == 'Октябрь' or month == 'Ноябрь' or day < 21 and month == 'Декабрь':
        print('Осень')
    elif day >= 21 and month == 'Декабрь' or month == 'Январь' or month == 'Февраль' or day < 20 and month == 'Март':
        print('Зима')
    else:
        print('Месяц отсутствует')
else:
    print('День отсутствует в календаре')
