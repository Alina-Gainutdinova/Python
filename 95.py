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
