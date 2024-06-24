import random
import string

def generate_password(min_length, number=True, special_character=True):
    letter=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    characters=letter
    if number:
        characters+=digits
    if special_character:
        characters+=special

    pwd=""
    meet_criteria=False
    has_number=False
    has_special=False

    while not meet_criteria or len(pwd)<min_length:
        new_char=random.choice(characters)
        pwd+=new_char
        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
        meet_criteria=True
        if number:
            meet_criteria=has_number
        if special_character:
            meet_criteria=meet_criteria and has_special

    return pwd
min_length=int(input("Enter the Minimum length\n"))
has_number=input("You want numbers in password? Press Y/N \n")=="y"
has_special=input("You want special character in password? Press Y/N \n")=="y"
pwd= generate_password(min_length,has_number,has_special)
print("Your Generated password is: ",pwd)