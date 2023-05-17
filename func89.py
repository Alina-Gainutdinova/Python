# # Перевод целых чисел в числительные упр 89
# def numerals(num):
#     if num >= 1 and num < 12:
#         if num == 1:
#             return "first"
#         elif num == 2:
#             return "second"
#         elif num == 3:
#             return "third"
#         elif num == 4:
#             return "fourth"
#         elif num == 5:
#             return "fifth"
#         elif num == 6:
#             return "sixth"
#         elif num == 7:
#             return "seventh"
#         elif num == 8:
#             return "eighth"
#         elif num == 9:
#             return "ninth"
#         elif num == 10:
#             return "tenth"
#         elif num == 11:
#             return "eleventh"
#     else:
#         return ""


# def main():
#     nums = int(input('Введите целое число от 1 до 12: '))
#     print(numerals(nums))


# if __name__ == '__main__':
#     main()

numeral = [
    "zero",
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eight",
    "ninth",
    "tenth",
    "eleventh",
]


def numerals(num):
    if 1 <= num < 12:
        return numeral[num]
    else:
        return ""


def main():
    nums = int(input("Введите целое число от 1 до 12: "))
    numerals(nums)
    i = 0
    for i in range(1, 12):
        print(numeral[i])


if __name__ == "__main__":
    main()
