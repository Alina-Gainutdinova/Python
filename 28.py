choice = int(
    input('Выберите единицы измерения ("1" - см/кг) / ("2" - дюймы/фунты): '))
if choice == 1:
    height_m = int(input('Введите ваш рост в см: '))
    weight_kg = float(input('Введите ваш вес в кг: '))
    print(
        f'Индекс массы вашего тела равен: {weight_kg / ((height_m / 100) ** 2)}')
elif choice == 2:
    height_inch = float(input('Введите ваш рост в дюймах: '))
    weight_funt = float(input('Введите ваш вес в фунтах: '))
    print(
        f'Индекс масы вашего тела равен: {weight_funt / (height_inch ** 2 ) * 703}')
