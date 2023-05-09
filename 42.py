note = input("Введите обозначение ноты: ")
x = int(input("Введите номер ноты: "))
note = note.capitalize()

if note == "C":
    print(f'{261.63 / 2**(4-x)}')
elif note == "D":
    print(f'{293.66 / 2**(4-x)}')
elif note == "E":
    print(f'{329.63 / 2**(4-x)}')
elif note == "F":    
    print(f'{349.23 / 2**(4-x)}')
elif note == "G": 
    print(f'{392.00 / 2**(4-x)}')
elif note == "A":   
    print(f'{440.00 / 2**(4-x)}')
elif note == "B":   
    print(f'{493.88 / 2**(4-x)}')         