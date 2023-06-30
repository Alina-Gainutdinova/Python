# def correct_sentence(sentence: str) -> str:
#     sentence = sentence.strip()  # Удаляем начальные и конечные пробелы

#     # Сделать заглавной первую букву в строке
#     if sentence:
#         sentence = sentence[0].upper() + sentence[1:]

#     # Сделать заглавными буквы после точки, восклицательного или вопросительного знака
#     for i in range(1, len(sentence)):
#         if sentence[i - 1] in ['.', '!', '?']:
#             sentence = sentence[:i] + sentence[i].upper() + sentence[i + 1:]

#     # Сделать заглавными буквы 'i', которым предшествует пробел или за которыми следует пробел, точка, восклицательный или вопросительный знак
#     words = sentence.split()
#     for i in range(len(words)):
#         if words[i] == 'i':
#             if i == 0 or words[i - 1][-1] in [' ', '.', '!', '?']:
#                 words[i] = words[i].upper()

#     return ' '.join(words)
# def main():
#     sentence = input('Введите предложение: ')
#     corrected_sentence = correct_sentence(sentence)
#     print(corrected_sentence)

def correct_sentence(sentence: str) -> str:
    sentence = sentence.strip() 
    result = ""

    capitalize_next = True  

    for i in range(len(sentence)):
        char = sentence[i]

        if char == "i":
            if i == 0 or sentence[i - 1] == " "  and sentence[i + 1] in [" ", ".", "!", "?", "'"]:
                char = char.upper()
            else:
                capitalize_next = False 

        if char in [".", "!", "?"]:
            capitalize_next = True

        result += char

    return result


def main():
    sentence = input('Введите предложение: ')
    corrected_sentence = correct_sentence(sentence)
    print(corrected_sentence)

main()
