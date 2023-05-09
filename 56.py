frequency = float(input('Введите значение частоты волны: '))

if frequency < 3 * 10**9:
    print('Радиоволны')
elif 3 * 10**9 > frequency < 3 * 10**12:
    print('Микроволны')
elif 3 * 10**12 > frequency < 4.3 * 10**14:
    print('Инфракрасное излучение')
elif 4.3 * 10**12 > frequency < 7.5 * 10**14:
    print('Видимое излучение')
elif 7.5 * 10**14 > frequency < 3 * 10**17:
    print('Ультрафиолетовое излучение')
elif 3 * 10**17 > frequency < 3 * 10**19:
    print('Рентгеновское излучение')
elif frequency > 3 * 10**19:
    print('Гамма излучение')
