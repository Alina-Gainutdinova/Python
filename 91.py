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