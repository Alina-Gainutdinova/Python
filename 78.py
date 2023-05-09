#from math import floor
#num = input("Введите целое число(нажмите 0 для выхода): ")
#num = 0
#while num >= 0:
    #while num != 1:
           # if num % 2 == 0:
               # num = floor(num / 2)
           # else:
              #  num = num * 3 + 1 
#print(list(num))                

# Гипотеза Коллатца. Напишите программу, которая будет запрашивать у пользователя целое число и  выводить все числа, начиная с  введенного числа и  заканчивая единицей.
import math
num = int(input('Enter number: '))

while num > 0:
    nums = []
    while num != 1:
        nums.append(num)
        if num % 2 == 0:
            num = math.floor(num / 2)
            nums.append(num)
        else:
            num = num * 3 + 1
            nums.append(num)
    print(nums)
    num = int(input('Enter number: '))
