number = input('Введите номерной знак автомобиля: ')

if number.isdigit() == True:
    print('Новый формат')
elif number.isdigit() == False:
    print('Старый формат')    
else:
    print('Не соответствует ни одному из двух форматов')