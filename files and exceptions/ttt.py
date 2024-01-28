import random

words = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'ab', 'cd']

w1 = ""
w2 = ""

while len(w1) <= 3 or len(w2) <= 3:
    w1 = random.choice(words)
    w2 = random.choice(words)

print("w1:", w1)
print("w2:", w2)
