# Плата за такси
def amount_for_a_taxi(distance):
    start_rate = 4.00
    variable_rate = 0
    summ = start_rate + (distance / 0.14) * 0.25
    if distance > 0.14:
        return summ
        
    else:
        return start_rate


def main():
    dist = float(input("Введите расстояние поездки в км: "))
    print(f'Итоговая сумма равна: ${amount_for_a_taxi(dist)}')
main()