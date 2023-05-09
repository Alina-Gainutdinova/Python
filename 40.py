decibels = int(input("Введите уровень шума в дБ: "))
if decibels == 130:
    print("Отбойный молоток")
elif decibels == 106:
    print("Газовая газонокосилка")
elif decibels == 70:
    print("Будильник")
elif decibels == 40:
    print("Тихая комната")
elif 106 < decibels < 130:
    print("Между отбойным молотком и газовой газонокосилкой")
elif 70 < decibels < 106:
    print("Между газовой газонокосилкой и будильником")
elif 40 < decibels < 70:
    print("Между будильником и тихой комнатой")
else:
    print("За пределами диапазона")
