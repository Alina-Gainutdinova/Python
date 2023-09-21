from exr115 import get_proper_divisors

def its_a_perfect_number(number):
    if number == sum(get_proper_divisors(number)):
        return True
    else:
        return False
print(its_a_perfect_number(28))    

perfect_nums = []

for i in range(0, 10001):
    if its_a_perfect_number(i):
        perfect_nums.append(i)
print(perfect_nums)        


