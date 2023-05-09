sec = int(input("Enter amounts of seconds: "))
days = sec // 86400
sec = sec % 86400
hours = sec // 3600
sec = sec % 3600
minutes = sec // 60
sec = sec % 60
print(f'{days} days {hours:02d}:{minutes:02d}:{sec:02d}')
