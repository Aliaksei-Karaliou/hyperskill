word = input()
output = ''
for letter in word:
    if letter.isupper():
        output += '_' + letter.lower()
    else:
        output += letter
print(output)
