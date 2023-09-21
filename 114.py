data = []
word = input("Введите число ('q' для окончания ввода): ")
while word != 'q':
    num = int(word)
    data.append(num)
    word = input("Введите число ('q' для окончания ввода): ")

print(sorted(data))
# negative_num = []
# zeros = []
# positive_num = []


# for i in data:
#     if i < 0:
#         negative_num.append(i)
#     elif i == 0:
#         zeros.append(i)
#     else:
#         positive_num.append(i)    

# new_data = negative_num + zeros + positive_num
# print(new_data)