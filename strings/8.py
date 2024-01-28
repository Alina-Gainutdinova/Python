souvenir = int(input("Enter amount souvenir: "))
bauble = int(input("Enter amount bauble: "))
total = souvenir * 0.075 + bauble * 0.112
print('%.3f' % total, 'kg', "=", total * 1000, 'gr')

print(f'{total:.3f} kg = {total * 1000} gr')
