import random

def generate_password():
    length = random.randint(7, 10)  
    password = ''
    for i in range(length):
        password += chr(random.randint(33, 126)) 
    return password

if __name__ == "__main__":
    password = generate_password()
    print(password)
