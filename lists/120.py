def format_list(str_list: list):
    if len(str_list) == 1:
        return ''.join(str_list)
    str_list[-2] = str_list[-2] + ' и'


    for i in range(len(str_list) - 2):
        str_list[i] = str_list[i] + ','

    str_ = ' '.join(str_list)
    return str_
def main():
    lst = []

    while True:
        words = input('Введите список слов(Enter для завершения): ')
        if words == '':
            break
        lst.append(words)
    print(format_list(lst))
main()    