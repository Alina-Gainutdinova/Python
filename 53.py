grade = float(input('Введите числовую оценку успеваемости: '))

if grade > 4.0:
    print('Буквенная оценка: A+')
elif 3.7 < grade <= 4.0:
    print('Буквенная оценка: A')
elif 3.3 < grade <= 3.7:
    print('Буквенная оценка: A-')
elif 3.0 < grade <= 3.3:
    print('Буквенная оценка: B+')
elif 2.7 < grade <= 3.0:
    print('Буквенная оценка: B')
elif 2.3 < grade <= 2.7:
    print('Буквенная оценка: B-')
elif 2.0 < grade <= 2.3:
    print('Буквенная оценка: C+')
elif 1.7 < grade <= 2.0:
    print('Буквенная оценка: C')
elif 1.3 < grade <= 1.7:
    print('Буквенная оценка: C-')
elif 1.0 < grade <= 1.3:
    print('Буквенная оценка: D+')
elif 0 < grade <= 1.0:
    print('Буквенная оценка: D')
elif 0 == grade:
    print('Буквенная оценка: F')
else:
    print('Предел диапазона')
