from random import random
from string import ascii_letters


def ask_password():
    length = int(input("Password length: "))
    symbols = (input("Use symbols? Y/N: "))
    if symbols.lower() == "yes" or symbols.lower() == "y":
        symbols = True
    elif symbols.lower() == "no" or symbols.lower() == "n":
        symbols = False
    generate_pass(length, symbols)


def generate_pass(length, symbols=False):
    password = ""
    symbol_pool = [
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
    ]
    for i in ascii_letters:
        symbol_pool.append(i)
    if symbols == False:
        for x in range(length):
            letter = int(52 * random())
            password += ascii_letters[letter]
    elif symbols == True:
        for x in range(length):
            letter = int((len(symbol_pool)) * random())
            password += symbol_pool[letter]
    print(password)
    return None


ask_password()
