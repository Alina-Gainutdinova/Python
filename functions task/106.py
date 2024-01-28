def days_in_a_month(m, y):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y % 4 == 0:
        months[1] = 29 
    return months[m - 1]

def main():
    num_month = int(input('Введите номер месяца: '))    
    year = int(input('Введите год: '))
    print(days_in_a_month(num_month, year))
main()    