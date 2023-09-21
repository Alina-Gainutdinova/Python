def get_proper_divisors(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return divisors

if __name__ == "__main__":
        num = int(input("Введите число: "))
        print(f'Собственные делители числа: {get_proper_divisors(num)}')


