
from math import log10
num_a = int(input("Write number a: "))
num_b = int(input("Write number b: "))
sum = int(num_a + num_b)
multi = int(num_a * num_b)
quotient = int(num_a / num_b)
remainder = int(num_a % num_b)
log = int(log10(num_a))
degree = int(num_a ** num_b)
print(f'Sum of numbers: {sum}\nMultiplication of numbers: {multi}\nQuotient of numbers: {quotient}\nRemainder of the division: {remainder}\nLogarithm of a number: {log}\nExpotentation: {degree}')
