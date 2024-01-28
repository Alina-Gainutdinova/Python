def strings(s, w):
    if len(s) >= w:
        return s 
    spaces = (w - len(s)) // 2
    res = " " * spaces + s
    return res

def main():
    str = input('Введите строку: ')
    wid = int(input('Введите ширину окна: '))
    print(strings(str, wid))    
main()