from t117 import removes_signs
file = input('Введите имя файла: ')

words = []  # слова, имеющиеся на одной строке в файле
all_words = []  # список слов words внутри одного списка
str_list = []  # слова без вложенных списков
new_list = []  # слова без знаков препинаний
same_words = []  # одинаковые слова

try:
    with open(f'{file}', 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            all_words.append(words)

        for words in all_words:
            str_list.extend(words)
        # print(str_list)

        for s in str_list:
            new_list.append(','.join(removes_signs(s)))
        # print(new_list)

        for i in range(len(new_list)):
            for j in range(i + 1, len(new_list)):
                if new_list[i] == new_list[j]:
                    same_words.append(new_list[j])
        print(f'Одинаковые слова в файле: {same_words}')

except:
    print('Ошибка при доступе к файлу')
