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
def main():
                     