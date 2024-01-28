def is_list_sorted(checked_list):
    sorted_ascending = sorted(checked_list)
    sorted_descending = sorted(checked_list, reverse=True)

    if checked_list == sorted_ascending or checked_list == sorted_descending:
        return True
    else:
        return False


list_nums = []


def main():
    while True:
        nums = input('Введите число (пустая строка для завершения): ')
        if nums == '':
            break
        list_nums.append(int(nums))
    print(list_nums)

    if len(list_nums) <= 1:
        print('Список пуст или имеется один элемент')
    elif is_list_sorted(list_nums):
        print('Список отсортирован изначально')
    else:
        print('Список не отсортирован изначально')


main()
