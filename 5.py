volume1 = int(input("Сколько бутылок до 1 литра?: "))
volume2 = int(input("Сколько бутылок больше 1 литра?: "))
price = volume1*0.1 + volume2*0.25
print(f'Прайс составляет: ${price:.2f}')
