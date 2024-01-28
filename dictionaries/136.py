def reverseLookup(dictionary, mean):
    keys_list = []
    for k, m in dictionary.items():
        if m == mean:
            keys_list.append(k)
    return f'Ключи значения {mean}: {keys_list}'


def main():
    dict_1 = {
        'name': 'Alina',
        'city': 'Tashkent',
        'age': 20,
        'job': 'programming',
        'hobby': 'programming',
        'date': 20,
    }
    print(reverseLookup(dict_1, 21))


main()
