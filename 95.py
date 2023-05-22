# def headline(text):
# text = input('....').split(" ")
# sign = ['.', '!', '?']
# i = 0
# for i in text:
#     if i == sign:
#         print(str(i.upper()))
#     i += 1
# print(headline('алина.малина'))    
        

def correct(txt: str):
    c = 1
    txt_ = ''
    for char in txt:
        if char in ['.','!', '?']:
            txt_ += char
            c = 1
        elif c == 1 and char.isalpha():
            txt_ += char.upper()
            c = 0
        else:
            txt_ += char
    return txt_
print(correct('hello!alina'))                    