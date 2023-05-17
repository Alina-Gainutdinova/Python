# 12 дней Рождества
from func89 import numerals
# Отображаем один куплет песни The Twelve Days of Christmas
# @param n – куплет для отображения
# @return (None)


def displayVerse(n):
    print("On the", numerals(n), "day of Christmas")
    print("my true love sent to me:")
    if n >= 12:
        print("Twelve drummers drumming,")
    if n >= 11:
        print("Eleven pipers piping,")
    if n >= 10:
        print("Ten lords a–leaping,")
    if n >= 9:
        print("Nine ladies dancing,")
    if n >= 8:
        print("Eight maids a–milking,")
    if n >= 7:
        print("Seven swans a–swimming,")
    if n >= 6:
        print("Six geese a–laying,")
    if n >= 5:
        print("Five golden rings,")
    if n >= 4:
        print("Four calling birds,")
    if n >= 3:
        print("Three French hens,")
    if n >= 2:
        print("Two turtle doves,")
    if n == 1:
        print("A", end=" ")
    else:
        print("And a", end=" ")
    print("partridge in a pear tree.")
    print()
# Отображаем все 12 куплетов песни


def main():
    for verse in range(1, 12):
        displayVerse(verse)


# Вызываем основную функцию
main()
