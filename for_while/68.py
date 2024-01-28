grade = input('Введите буквенную оценку успеваемости(Enter для остановки): ')
num = 0
sum = 0.0
amount = 0

while grade != "":
    grade = input('Введите буквенную оценку успеваемости(Enter для остановки): ')
    if grade == 'A+':
        num += 4.0
    elif grade == 'A':
        num += 4
    elif grade == 'A-':
        num += 3.7
    elif grade == 'B+':
        num += 3.3
    elif grade == 'B':
        num += 3.0
    elif grade == 'B-':
        num += 2.7
    elif grade == 'C+':
        num += 2.3
    elif grade == 'C':
        num += 2.0
    elif grade == 'C-':
        num += 1.7
    elif grade == 'D+':
        num += 1.3    
    elif grade == 'D':
        num += 1.0
    elif grade == 'F':
        num += 0                
sum += num    
amount += 1
print(f'Средняя оценка равна: {sum/amount}')
