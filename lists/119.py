def between_average():
    average_down = []
    average_up = []
    equal_average = []
    list_num = []
   
    
    while True:
        s = input('Введите числа (нажмите Enter, чтобы завершить ввод): ')
        if s == '':
            break
        s = int(s)
        list_num.append(s)
        
    average = sum(list_num) / len(list_num)
    
    for num in list_num:
        if num > average:
            average_down.append(num)
        elif num == average:
            equal_average.append(num)
        elif num < average:
            average_up.append(num)
    
    print(average_down)
    print(equal_average)
    print(average_up)

between_average()



