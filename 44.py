nominal = int(input("Введите номинал банкноты: "))

if nominal == 1:
    print("Джордж Вашингтон")
elif nominal == 2:
    print("Томас Джеферсон")
elif nominal == 5:
    print("Авраам Линкольн")
elif nominal == 10:
    print("Александр Гамильтон")
elif nominal == 20:
    print("Эндрю Джексон")
elif nominal == 50:
    print("Уилисс Грант")
elif nominal == 100:
    print("Бенджамин Франклин")
else:
    print("Ошибка")
