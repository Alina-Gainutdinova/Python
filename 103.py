from exercise100 import generate_password
from exercise102 import password_strength

def generate_strong_password():
    attempts = 0
    while True:
        password = generate_password()
        attempts += 1
        if password_strength(password):
            return password, attempts

if __name__ == "__main__":
    password, attempts = generate_strong_password()
    print(f"Сгенерированный надежный пароль: {password}")
    print(f"Количество попыток: {attempts}")
