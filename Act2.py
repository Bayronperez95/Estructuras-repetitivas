texto = 'hello-world'

for char in texto:
    if not char.isalpha():
        print('Non-alphabetic char found!')
        break
else:
    print('All chars are alphabetic')