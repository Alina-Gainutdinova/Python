import copy 
list_num = []
def remove_outliers(list_nums):
    copy_list = copy.copy(list_nums)
    copy_list.remove(min(list_nums))
    copy_list.remove(max(list_nums))
    if len(list_num) < 4:
        return 'Ошибка! Введите не менее 4 чисел'
    else:
        return copy_list

def main():
    while True:
        num_str = input('Введите числа(Enter для завершения): ')
        if num_str == '':
            break
        num = int(num_str)
        list_num.append(num)
    print(list_num)
    print(remove_outliers(list_num))        
main()    