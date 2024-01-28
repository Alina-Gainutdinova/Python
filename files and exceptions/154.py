file = input('Введите имя файла: ')
labels = {}
other_sym = ["", ".", "!", "?", ",", "'", "\n", "-"]
try:
    with open(f'{file}', 'r') as f:
        lines = f.readlines()
        for line in lines:
            for l in line.lower():
                if l in other_sym:
                    continue
                elif l not in labels:
                    labels[l] = 1
                else:
                    labels[l] += 1
        print(f'Частота букв: {labels}')
except:
    print('Ошибка при доступе к файлу')
