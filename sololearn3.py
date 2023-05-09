humidity = int(input("Enter humidity: "))
if humidity >= 40 and humidity <= 60:
    print("Norm")
elif humidity <= 0:
    print("Bad")
else:
    print("Dampness")    
    