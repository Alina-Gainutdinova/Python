from random import randint


def generate_nums():
    lotto_cards = {
        'B': [randint(1, 15) for i in range(5)],
        'I': [randint(16, 30) for i in range(5)],
        'N': [randint(31, 45) for i in range(5)],
        'G': [randint(46, 60) for i in range(5)],
        'O': [randint(61, 75) for i in range(5)]
    }
    lst = []
    for i in range(5):
        b = randint(0, 15)
        lst.append(b)
    print(lst)


generate_nums()


def print_loto_cards():
    pass


def main():
    pass
