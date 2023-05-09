change = int(input("Enter change amount: "))

TOONIE = 200
LOONIE = 100
TWENTY_FIVE = 25
TEN = 10
FIVE = 5
ONE = 1

toonie = change // TOONIE
change %= TOONIE
loonie = change // LOONIE
change %= LOONIE
twenty_five = change // TWENTY_FIVE
change %= TWENTY_FIVE
ten = change // TEN
change %= TEN
five = change // FIVE
change %= FIVE
one = change // ONE

print(f'{toonie} toonie, {loonie} loonie, {twenty_five} 25cent, {ten} 10cent, {five} 5cent, {one} 1cent')
