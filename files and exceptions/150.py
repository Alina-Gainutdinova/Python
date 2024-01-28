import sys
NUM_LINES = 5
if len(sys.argv) != 2:
    print("Передайте имя файла в качестве аргумента командной строки.")
    quit()
try:
    inf = open(sys.argv[1], "r")

    lines = []
    for line in inf:
        lines.append(line)
        if len(lines) > NUM_LINES:
            lines.pop(0)
            print(lines)

    inf.close()
except:
    print("Ошибка при доступе к файлу.")
    quit()

for line in lines:
    print(line, end="")
