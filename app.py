from flask import Flask
app = Flask(__name__)
import random
@app.route("/")
def hello():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    type_of_character=["letters","numbers","symbols"]
    total=sum([nr_numbers,nr_symbols,nr_letters])
    password=""
    if nr_numbers==0:type_of_character.remove("numbers")
    if nr_symbols==0:type_of_character.remove("symbols")
    if nr_letters==0:type_of_character.remove("letters")
    for times in range(total):
        chosen_type=random.choice(type_of_character)
        print(chosen_type)
        if chosen_type=="letters":
            nr_letters -=1
            password += random.choice(letters)
            if nr_letters==0:
                 type_of_character.remove("letters")
        elif  chosen_type=="numbers":
            nr_numbers -=1
            password += random.choice(numbers)
            if nr_numbers==0:
                    type_of_character.remove("numbers")
        else :
            nr_symbols -= 1
            password += random.choice(symbols)
            if nr_symbols == 0:
                type_of_character.remove("symbols")
    print(password)
