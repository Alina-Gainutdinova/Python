from exr115 import get_proper_divisors

def is_a_perfect_num(number):
    if number == sum(get_proper_divisors(number)):
        return True
    else:
        return False
print(is_a_perfect_num(28))    

perfect_nums = []

for i in range(0, 10001):
    if is_a_perfect_num(i):
        perfect_nums.append(i)
print(perfect_nums)        


