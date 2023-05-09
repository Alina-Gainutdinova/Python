day = int(input('Введите день рождения: '))
month = input('Введите месяц рождения: ')

if 0 < day <= 31:
    if day >= 22 and month == 'декабря' or day <= 19 and month == 'января':
        print('Козерог')
    elif day >= 20 and month == 'января' or day <= 18 and month == 'февраля':
        print('Водолей')   
    elif day >= 19 and month == 'февраля' and day <= 28 or day <= 20 and month == 'марта':  
        print('Рыбы')  
    elif day >= 21 and month == 'марта' or day <= 19 and month == 'апреля':
        print('Овен')
    elif day >= 20 and month == 'апреля' or day <= 20 and month == 'мая':    
        print('Телец')
    elif day >= 21 and month == 'мая' or day <= 20 and month == 'июня':    
        print('Близнецы')
    elif day >= 21 and month == 'июня' or day <= 22 and month == 'июля':   
        print('Рак')
    elif day >= 23 and month == 'июля' or day <= 22 and month == 'августа':  
        print('Лев')  
    elif day >= 23 and month == 'августа' or day <= 22 and month == 'сентября':   
        print('Дева') 
    elif day >= 23 and month == 'сентября' or day <= 22 and month == 'октября':    
        print('Весы')
    elif day >= 23 and month == 'октября' or day <= 21 and month == 'ноября':  
        print('Скорпион')  
    elif day >= 22 and month == 'ноября' or day <= 22 and month == 'декабря':    
        print('Стрелец')
    else:
        print('Введены неверные данные')    
else:
    print('Предел диапазона')       