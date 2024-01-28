def unique_symbols(line):
    sym = set(line)
    return len(sym)


def main():
    msg = input('Введите сообщение: ')
    print(unique_symbols(msg))


main()
