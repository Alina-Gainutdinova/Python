# def correct(txt: str):
#     c = 1
#     txt_ = ''
#     for char in range(len(txt)):
#         if txt[char] in ['.','!', '?']:
#             txt_ += char
#             c = 1
#         elif c == 1 and char.isalpha() or txt[-char] == " " and txt[char] == 'i':
#             txt_ += char.upper()
#             c = 0
#         else:
#             txt_ += char
#     return txt_


# def main():
#     text = input('Введите текст: ')
#     print(correct(text))   
# main()    

def correct(txt: str):
    c = 1
    txt_ = ''
    for char in range(len(txt)):
        if txt[char] in ['.', '!', '?']:
            txt_ += txt[char]  # Исправлено: добавлен символ строки, а не индекс
            c = 1
        elif (c == 1 and txt[char].isalpha()) or (txt[char] == 'i' and txt[char-1] == ' ' and txt[char + 1] == "'" or txt[char + 1] == ' '):
            txt_ += txt[char].upper()
            c = 0
        # elif txt[char] == 'i' and txt[char-1] == ' ' and txt[char + 1] == "'":
        #     txt_ += txt[char].upper()  # Исправлено: добавлен символ строки, а не индекс
        #     c = 0
        else:
            txt_ += txt[char]  # Исправлено: добавлен символ строки, а не индекс
    return txt_

def main():
    text = input('Введите текст: ')
    print(correct(text))

main()
