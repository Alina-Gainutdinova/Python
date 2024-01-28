read_file = input('Введите имя исходного файла: ')
write_file = input('Введите имя целевого файла: ')


with open(f'{read_file}', 'r') as fr, open(f'{write_file}', 'w') as fw:
    lines = fr.readlines()
    i = 1
    for line in lines:
        new_line = f'{i}: {line}'
        fw.write(new_line)
        i += 1
