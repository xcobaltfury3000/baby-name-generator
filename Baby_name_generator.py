print ("Hello world")

import string

print(string.ascii_letters)

print(string.ascii_lowercase)
#since we want a random selection we import random
import random
#from random library we want to utilize choice method
print(random.choice("pullaletterfromhere"))
print(random.choice(string.ascii_lowercase))

letter_input_1 = input('choose a letter: "v" for vowel "c" for consonant "l" for any other letter')
letter_input_2 = input('choose a letter: "v" for vowel "c" for consonant "l" for any other letter')
letter_input_3 = input('choose a letter: "v" for vowel "c" for consonant "l" for any other letter')
letter_input_4 = input('choose a letter: "v" for vowel "c" for consonant "l" for any other letter')
letter_input_5 = input('choose a letter: "v" for vowel "c" for consonant "l" for any other letter')

vowels = 'aeiouy'
consonant = 'bcdfghjklmnpqrstvwxz'
letter = string.ascii_lowercase


# copy conditional loop for the rest of the letter inputs

def generator():


    if letter_input_1 == "v":
        letter1 = random.choice(vowels)
    elif letter_input_1 == "c":
        letter1 = random.choice(consonant)
    elif letter_input_1 == "l":
        letter1 = random.choice(letter)
    else:
        letter1 = letter_input_1  # allows user to put a specific letter

    if letter_input_2 == "v":
        letter2 = random.choice(vowels)
    elif letter_input_2 == "c":
        letter2 = random.choice(consonant)
    elif letter_input_2 == "l":
        letter2 = random.choice(letter)
    else:
        letter2 = letter_input_2

    if letter_input_3 == "v":
        letter3 = random.choice(vowels)
    elif letter_input_3 == "c":
        letter3 = random.choice(consonant)
    elif letter_input_3 == "l":
        letter3 = random.choice(letter)
    else:
        letter3 = letter_input_3

    if letter_input_4 == "v":
        letter4 = random.choice(vowels)
    elif letter_input_4 == "c":
        letter4 = random.choice(consonant)
    elif letter_input_4 == "l":
        letter4 = random.choice(letter)
    else:
        letter4 = letter_input_4

    if letter_input_5 == "v":
        letter5 = random.choice(vowels)
    elif letter_input_5 == "c":
        letter5 = random.choice(consonant)
    elif letter_input_5 == "l":
        letter5 = random.choice(letter)
    else:
        letter5 = letter_input_5

    name =letter1 + letter2+letter3+letter4+letter5
    return(name)

for i in range (20): # to generate 20 different names

    print(generator())

