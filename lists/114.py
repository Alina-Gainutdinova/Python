data = []
word = input("Введите число ('q' для окончания ввода): ")
while word != 'q':
    num = int(word)
    data.append(num)
    word = input("Введите число ('q' для окончания ввода): ")

print(sorted(data))
