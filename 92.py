def back_ordinal_date(date):
    year = int(date / 1000)
    day = date % 1000
    print(year)
    print(day)









def main():
    ord_dt = int(input('Введите порядковую дату: '))
    back_ordinal_date(ord_dt)
main()    