age = input('Введите ваш возраст(Enter для остановки): ')
ticket = 0
total = 0
year = int(age)

while age != "":
    age = input('Введите возраст следующего посетителя(Enter для остановки): ')
    if 3 <= year <= 12:
        ticket += 14.00
    elif year > 65:
        ticket += 18.00
    elif year <= 2:
        ticket += 0
    else:
        ticket += 23.00
total += ticket       
print(f'Общая сумма билетов: $ {total}')
        