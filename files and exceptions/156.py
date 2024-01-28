line = input("Введите число: ")
total = 0

while line != "":
    try:
        num = float(line)
        total += num
        print("Сумма сейчас составляет", total)
    except ValueError:
        print("Это было не число")

    line = input("Введите число: ")

print("Общая сумма:", total)
