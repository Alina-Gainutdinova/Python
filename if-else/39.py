month = input("Введите название месяца: ")
month = month.capitalize()

if month == "Январь" or month == "January" or month == "Март" or month == "March" or month == "Май" or month == "May" or month == "Июль" or month == "July" or month == "Август" or month == "August" or month == "Октябрь" or month == "October" or month == "Декабрь" or month == "December":
    print(31)
elif month == "Февраль" or month == "February":
    print('28/29')
elif month == "Апрель" or month == "April" or month == "Июнь" or month == "June" or month == "Сентябрь" or month == "September" or month == "Ноябрь" or month == "November":
    print(30)
else:
    print("Неверное название месяца")
