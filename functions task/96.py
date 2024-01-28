def isInteger(s):
    for char in s.strip():
        if char == '+' or char == '-':
            continue
        elif not char.isdigit():
            return False
    return True    

def main():
    txt = input('Введите строку: ')
    print(isInteger(txt))

if __name__ == "__main__":
    main()    
