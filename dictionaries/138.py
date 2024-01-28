def sequence_of_buttons():
    buttons = {
        '1': ['.', ',', '?', '!', ':'],
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z'],
        '0': ['']
    }
    msg = input('Введите сообщение: ').upper()

    num_of_buttons = ''
    for s in msg:
        for k, m in buttons.items():
            if s in m:
                num_of_buttons += k * (m.index(s) + 1)
            else:
                continue

    print(num_of_buttons)


sequence_of_buttons()
