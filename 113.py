data = []
word = input("Введите слово (Enter для окончания ввода): ")
while word != '':
    data.append(word)
    word = input("Введите слово (Enter для окончания ввода): ")

new_data = []

for s in data:
    if s not in new_data:
        new_data.append(s)
data = new_data
print(*new_data)        