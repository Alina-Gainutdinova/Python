line=input("enter: ")
digit_counter = 0
for i in line:
    i.isdigit()
    digit_counter+=1
    if digit_counter == 0:
        print("числа не обнаружены")
    else:
        print(digit_counter)