import string
from random import randint

alphabet = string.ascii_uppercase
for letter in alphabet:
    filename = f'{letter}.txt'
    with open(filename, 'w') as file:
        file.write(str(randint(1,100)))