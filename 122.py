consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j',
              'k', 'l', 'm', 'n', 'p', 'q', 'r',
              's', 't', 'v', 'w', 'x', 'y', 'z']

vowels = ['a', 'e', 'i', 'o', 'u']


def translation_into_Pig_latin(word):
    if word[0] in vowels:
        word += 'way'
        return word
    elif word[0] in consonants:
        for letter in word:
            if letter in consonants:
                word = word.replace(letter, '')
                word += letter
            else:
                break
        return word + 'ay'


def main():
    words = input('Введите строку: ')
    print(translation_into_Pig_latin(words))


if __name__ == "__main__":
    main()
