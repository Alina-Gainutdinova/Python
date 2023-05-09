num = float(input('Введите числа(0 для остановки ввода): '))

if num == 0:
   print("Error")
sum = 0
amount = 0

while num != 0:
    sum += num
    amount += 1
    num = float(input('Введите числа(0 для остановки ввода): '))

print('Среднее значение:', sum / amount)
