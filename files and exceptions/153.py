file = input('Введите имя файла: ')

with open(f'{file}', 'r', encoding='utf-8') as f:
    word_len = []
    lines = []
    for line in f.readlines():
        word_len.append(len(line.strip()))
        lines.append(line.strip())
        max_len = max(word_len)
    print(f'Длина самого длинного слова: {max_len}')
    max_len_words = list(filter(lambda line: len(line) == max_len, lines))
    print(f"Самые длинные слова: {', '.join(max_len_words)}")
