age = int(input("Введите человеческий год: "))
if 1 <= age <= 2:
    print(f"Равен {age * 10.5} годам собаки")
elif age > 2:
    res = (21 + (age - 2) * 4)
    print(f'Собачий возраст равен: {res}')
else:
    print("Ошибка!")
