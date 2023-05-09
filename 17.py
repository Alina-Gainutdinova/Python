m = float(input("Enter mass of water: "))
t = float(input("Enter temperature difference: "))
q = m * 4.186 * t 
price = (q * 2.778 * 10**(-7)) * 8.9
q1 = (0.2 * 1.35 * 85) * 8.9 
print(f'The amount of energy is: {q} joule\nThe cost of heating of water is: {price} cents\nThe cost of heating one cup of coffe is: {q1} cents ')