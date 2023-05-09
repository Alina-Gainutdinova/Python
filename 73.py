sms = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

new_sms = ""
for ch in sms:
    if ch >= "a" and ch <= "z":
        pos = ord(ch) - ord("a")
        pos = (pos + shift) % 26
        new_char = chr(pos + ord("a"))
        new_sms += new_char
    elif ch >= "A" and ch <= "Z":
        pos = ord(ch) - ord("A")
        pos = (pos + shift) % 26
        new_char = chr(pos + ord("A"))
        new_sms += new_char    
    else:
        new_sms += ch
print(f'Новое сообщение {new_sms}')          