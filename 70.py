byte = input('Введите комбинацию из 8 бит(Enter для остановки): ')

while byte != "":

    if byte.count("1") + byte.count("0") != 8 or len(byte) != 8:
        print("Это не 8 бит. Повторите попытку")
    else:
        ones = byte.count("1")
    
        if ones % 2 == 0:
            print('Бит четности должен иметь значение 0.')
        else:
            print('Бит четности должен иметь значение 1.') 

    byte = input('Введите комбинацию из 8 бит(Enter для остановки): ')        
    