month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def ordinalDate(date, month, year):
    acc_days = date
    if is_leap_year(year):
        acc_days += 1
    for i in range(month - 1):
        acc_days += month_day[i]
    return acc_days


def main():
    dt = int(input("Введите дату: "))
    mth = int(input("Введите месяц: "))
    yr = int(input("Введите год: "))
    print(f"Порядковый номер дня: {ordinalDate(dt, mth, yr)}")


if __name__ == "__main__":
    main()
