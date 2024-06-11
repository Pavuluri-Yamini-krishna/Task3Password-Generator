import string
import random

def generate_password(length, character_set):
    characters = ''
    if '1' in character_set:
        characters += string.ascii_letters
    if '2' in character_set:
        characters += string.digits
    if '3' in character_set:
        characters += string.punctuation
    return ''.join(random.choices(characters, k=length))

print("Select random character to generate password : ")
print("1. Letters")
print("2. Digits")
print("3. Special characters")
print("4. Exit")

length = None
while True:
    try:
        length = int(input("Enter maximum length of the password: "))
        if length <= 0:
            print("Length specified as positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

while True:
    character_set_input = input("Enter random character to password generator: ")
    character_set = character_set_input.split(',')
    
    if '4' in character_set:
        print("Exit the program.")
        exit()
    
    if set(character_set).issubset({'1', '2', '3'}):
        break
    else:
        print("Invalid input! Please select from 1, 2, 3, 4.")

password = generate_password(length, character_set)

print("Finally! The random generated password is:", password)
