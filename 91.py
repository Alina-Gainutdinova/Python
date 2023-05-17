def ordinalDate(date, month, year):
    month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        md = 0
        for i in range(month -1):
            md += month_day[i]
        return md + date
    else:
        md = 0
        for i in range(month -1):
            md += month_day[i]
        return md + date - 1
    
   
        

def main():
    dt = int(input("Введите дату: "))
    mth = int(input("Введите месяц: "))
    yr = int(input("Введите год: "))
    print(f'Порядковый номер дня: {ordinalDate(dt, mth, yr)}')
main()