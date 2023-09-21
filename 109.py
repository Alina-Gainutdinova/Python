def magic_date(date, month, year):

    if date * month == int(year[-2:]):
        return 'Dates is magic'
    else:
        return 'Dates is simple'


def main():
    d = int(input('Enter day: '))
    m = int(input('Enter month: '))
    y = input('Enter year: ')
    print(magic_date(d, m, y))
main()