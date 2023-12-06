# >>> 22.03.2004
# 82
from task91 import ordinalDate
date = input('Enter date: ').split('.')
day = int(date[0])
month = int(date[1])
year = int(date[2])
print(ordinalDate(day, month, year))
