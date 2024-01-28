from t91 import month_day, is_leap_year, ordinalDate


def back_ordinal_date(date: list):
    year = int(date[0])
    day = int(date[1])
    if is_leap_year(year):
        day -= 1
    i = 0
    month = 1
    while day > 31:
        day -= month_day[i]
        i += 1
        month += 1
        if month > 12:
            i = 0
            month = 1
            year += 1
    return day, month, year


def main():
    # ord_dt = input("Введите год и порядковый день (через пробел): ").split(" ")
    # print(back_ordinal_date(ord_dt))
    print("--------------------------------------------------")
    purchase_date = input("Введите дату покупки: ").split(".")
    day = int(purchase_date[0])
    month = int(purchase_date[1])
    year = int(purchase_date[2])
    od = ordinalDate(day, month, year)
    expiration_date = int(input("Введите срок гарантии: "))
    print(back_ordinal_date([year, od + expiration_date]))


main()
