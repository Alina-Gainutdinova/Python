# # григорианский календарь в порядковый
# def ordinalDate(date, month, year):

#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         if 1 <= date < 31 and month == 1:
#             return date
#         elif 1 <= date <= 28 and month == 2:
#             return date + 31
#         elif 1 <= date <= 31 and month == 3:
#             return date + 31 + 28
#         elif 1 <= date <= 30 and month == 4:
#             return date + 31 + 28 + 31
#         elif 1 <= date <= 31 and month == 5:
#             return date + 31 + 28 + 31 + 30
#         elif 1 <= date <= 30 and month == 6:
#            return date + 31 + 28 + 31 + 30 + 31
#         elif 1 <= date <= 31 and month == 7:
#             return date + 31 + 28 + 31 + 30 + 31 + 30
#         elif 1 <= date <= 31 and month == 8:
#             return date + 31 + 28 + 31 + 30 + 31 + 30 + 31
#         elif 1 <= date <= 30 and month == 9:
#            return date + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
#         elif 1 <= date <= 31 and month == 10:
#             return date + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
#         elif 1 <= date <= 30 and month == 11:
#             return date + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
#         elif 1 <= date <= 31 and month == 12:
#             return date + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
#     else:
#         return date - 1


def ordinalDate(date, month, year):
    feb = 28
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        feb = 29
    month_day = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    acc = date
    for i in range(month - 1):
        acc += month_day[i]
    return acc


def main():
    dt = int(input("Введите день: "))
    mth = int(input("Введите месяц: "))
    yr = int(input("Введите год: "))
    print(f'Порядковый номер дня: {ordinalDate(dt, mth, yr)}')


if __name__ == '__main__':
    main()
