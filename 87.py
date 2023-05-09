# Расчёт стоимости доставки
def shipping_amount(numb_of_goods):
    first = 10.95 
    summ = first + 2.95 * (numb_of_goods - 1) 
    if numb_of_goods > 1:
        return summ
    else:
        return first        

def main():
    numb = int(input("Введите количество товаров в заказе: "))
    print(f'Общая сумма заказа: {shipping_amount(numb)}')
main()