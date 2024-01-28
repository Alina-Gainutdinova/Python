import string, random

letters = list(string.ascii_uppercase)
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def old_format():
    letter = random.choices(letters, k = 3)
    num1 = random.choices(nums, k = 3)
    return letter + num1


def new_format():
    letter = random.choices(letters, k = 3)
    num2 = random.choices(nums, k = 4)
    return num2 + letter
     

def main():
    numbers = random.randint(1, 2)
    if numbers == 1:
        print(old_format())
    else:
        print(new_format())    

main()            