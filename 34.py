amount = int(input("Введите количество купленных вчерашних буханок хлеба: "))
print(f'Цена за буханку хлеба: $3.42\nЦена со скидкой: ${3.42 * 60 / 100:.2f}\nОбщая стоимость приобетённого хлеба: ${amount * 3.42 * 60 / 100:.2f}')