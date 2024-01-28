file = input('Введите название файла: ')
new_file = input('Введите название файла назначения: ')

with open(f'{file}', 'r') as f, open(f'{new_file}', 'w') as fw:
    lines = f.readlines()
    for line in lines:
        if line[0] == '#' or line[-2] == '#':
            line.replace('\n', '')
        else:
            fw.write(line)
