def precedence(txt):
    if txt == '+' or txt == '-':
        return 1
    elif txt == '*' or txt == '/':
        return 2
    elif txt == '^':
        return 3
    else:
        return -1

def main():
    str_ = input('Введите оператор: ')
    print(precedence(str_))

if __name__ == "__main__":
    main()    