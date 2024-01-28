deposit = float(input("Enter your deposit: "))
bill1 = deposit * 0.04 + deposit
bill2 = bill1 * 0.04 + bill1
bill3 = bill2 * 0.04 + bill2
print(f'Сумма депозита за 1 год составляет: {bill1:.2f}')
print(f'Сумма депозита за 2 год составляет: {bill2:.2f}')
print(f'Сумма депозита за 3 год составляет: {bill3:.2f}')