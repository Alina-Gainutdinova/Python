grade = input('Введите буквенную оценку успеваемости: ').capitalize()

if grade == 'A+':
    print('Числовая оценка: 4.0')
elif grade == 'A':
    print('Числовая оценка: 4.0')
elif grade == 'A-':
    print('Числовая оценка: 3.7')
elif grade == 'B+':
    print('Числовая оценка: 3.3')
elif grade == 'B':
    print('Числовая оценка: 3.0')
elif grade == 'B-':
    print('Числовая оценка: 2.7')
elif grade == 'C+':
    print('Числовая оценка: 2.3')
elif grade == 'C':
    print('Числовая оценка: 2.0')
elif grade == 'C-':
    print('Числовая оценка: 1.7')
elif grade == 'D+':
    print('Числовая оценка: 1.3')
elif grade == 'D':
    print('Числовая оценка: 1.0')
elif grade == 'F':
    print('Числовая оценка: 0')
else:
    print('Неверная буква')
