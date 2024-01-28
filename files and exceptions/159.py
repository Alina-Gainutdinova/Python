import random
file = input('Введите название файла: ')

with open(f'{file}', 'r') as f:
    lines = f.readlines()
    words = [line.strip() for line in lines]

    w1 = ""
    w2 = ""

    while len(w1) < 3 or len(w2) < 3:
        w1 = random.choice(words)
        w2 = random.choice(words)
        password = w1.capitalize() + w2.capitalize()
        # if 8 >= len(password) >= 10:
        print(password)
