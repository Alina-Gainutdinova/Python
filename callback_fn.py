num = 0
res = []


def num_is_even(num):
    return num % 2 == 0


def filter(list_num, callback):
    for num in list_num:
        if callback(num):
            res.append(num)
    return res


ls_num = [2, 4, 10, 19, 82, 46, 53, 88]
print(filter(ls_num, num_is_even))
