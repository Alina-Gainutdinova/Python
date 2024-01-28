from math import sqrt 
x = int(input('Введите число x: '))
for i in range(x):
    guess = x / 2
    guess = (guess + x / guess) / 2
    guess = sqrt(x)
print(guess) 