import getpass
def password_strength(p):
    lenght = False
    has_digit = False
    has_upper = False
    has_lower = False
    if len(p) >= 8:
        lenght = True
    
    for i in p:
        if i.isupper():
            has_upper = True
        elif i.islower():
            has_lower = True
        elif i.isdigit():
            has_digit = True
    return lenght and has_digit and has_lower and has_upper

    
def main():
    password = getpass.getpass('Введите пароль: ')
    print(password, password_strength(password))
if __name__ == "__main__":
    main()