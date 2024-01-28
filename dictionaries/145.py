def scrabble(line):
    cost_of_letters = {
        1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: 'K',
        8: ['J', 'X'],
        10: ['Q', 'Z']
    }
    count = 0
    for k, v in cost_of_letters.items():
        for s in line:
            if s in v:
                count += k
    return count


def main():
    word = input('Введите слово: ').upper()
    print(scrabble(word))


main()
