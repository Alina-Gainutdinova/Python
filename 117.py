data = []
def removes_signs(words):
    str_ = ''
    for s in words:
        if s not in (':', '!', '?', ',', '.', ';', '-'):
            str_ += s    
    data = str_.split()
    return data 

def main():
    string = input('Введите строку: ')
    print(removes_signs(string))
main()    