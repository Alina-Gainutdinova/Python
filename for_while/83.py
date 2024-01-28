from random import randrange
num = 100
max_num = randrange(1, num + 1)
print(max_num)

num_updates = 0
for i in range(1, num):
    current = randrange(1, num + 1)

    if current > max_num:
        max_num = current
        max_num = num_updates + 1
        print(current, '<== Обновление')    
    else:
        print(current)    

print("Максимальное значение в ряду:", max_num)
print("Количество смен максимального значения:", num_updates)        