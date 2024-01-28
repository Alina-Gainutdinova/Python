def determine_post_code(code):
    post_codes = {
        'Ньюфаундленд': 'A',
        'Новая Шотландия': 'B',
        'Остров Принца Эдуарда': 'C',
        'Нью-Брансуик': 'E',
        'Квебек': ('G', 'H', 'J'),
        'Онтарио': ['K', 'L', 'M', 'N', 'P'],
        'Манитоба': 'R',
        'Саскачеван': 'S',
        'Альберта': 'T',
        'Британская Колумбия': 'V',
        'Нунавут': 'X',
        'Северо-Западные территории': 'X',
        'Юкон': 'Y'
    }
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for k, v in post_codes.items():
        if code[0] in v:
            print(k)

    if code[1] == '0':
        print('Сельская местность')
    elif code[1] not in nums:
        print('Индекс не верный')
    else:
        print('Город')


def main():
    post_code = input('Введите почтовый индекс: ').upper()
    determine_post_code(post_code)


main()
