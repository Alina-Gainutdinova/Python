length = int(input('Введите значение длины волны: '))

if 380 <= length < 450:
    print('Фиолетовый')
elif 450 <= length < 495:
    print('Синий')
elif 495 <= length < 570:
    print('Зеленый')
elif 570 <= length < 590:
    print('Желтый')
elif 590 <= length < 620:
    print('Оранжевый')
elif 620 <= length < 750:
    print('Красный')
else:
    print('Невидимая зона спектра')
