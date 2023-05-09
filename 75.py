text = input('Введите строку: ')
palindrome = True
i = 0

while i < len(text) / 2 and palindrome:
    if text[i] != text[len(text) - i - 1]:
        palindrome = False

    i += 1
if palindrome:
    print(text, " – это палиндром")
else:
    print(text, " – это не палиндром")    