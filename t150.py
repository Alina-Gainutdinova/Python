# input("Enter file name: ")
# filename = "C:/Users/Рустам/Desktop/Python/data.txt"
f_name = 'data.txt'

try:
    with open(f"{f_name}", "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(len(lines))
        for i, index in enumerate(range(10), 1):
            print(f"{i}) {lines[-10 + index].strip()}")
except:
    print("Нет такого файла")
