def is_prime(n):
    if n <= 1:  
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            return False
    return True  

if __name__ == "__main__":
    num = int(input("Введите целое число: "))
    if is_prime(num):
        print("Число является простым.")
    else:
        print("Число не является простым.")