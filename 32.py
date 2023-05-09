num = int(input("Введите четырехзначное число: "))
thousand = num // 1000
num %= 1000
hundred = num // 100
num %= 100
ten = num // 10
num %= 10
sum = thousand + hundred + ten + num
print(f'{thousand} + {hundred} + {ten} + {num} = {sum}')
# применение цикла----------------------------------
# num = input("Введите четырехзначное число: ")
# res = 0
# for i in num:
#     res += int(i)

# print(res)
