day = int(input("Введите день: "))
month = input("Введите месяц: ")

if day == 1 and month == "января":
    print("Новый год")
elif day == 1 and month == "июля":
    print("День Канады")
elif day == 25 and month == "декабря":
    print("Рождество")
else:
    print("Нет праздников")
