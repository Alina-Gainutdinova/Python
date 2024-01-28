files_name = input("Введите названия файлов: ").split(" ")

print(files_name)

try:
    file_1 = open(files_name[0], "r")
    file_2 = open(files_name[1], "r")
    new_file = open("result.txt", "w")
    for line in file_1:
        new_file.write(line)
    for line in file_2:
        new_file.write(line)
except:
    print("Что-то не то :(")
else:
    print("Данные успешно записаны")
finally:
    new_file.close()
    file_1.close()
    file_2.close()
