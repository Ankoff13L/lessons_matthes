import json


def numbers_user():
    """выводит любимое число пользователя."""
    filename = 'numbers_favorit.json'
    try:
        with open(filename) as f:
            filename = json.load(f)
    except FileNotFoundError:
        favorite_number = input("Enter your favorite number: ")
        with open(filename, 'w') as f:
            json.dump(favorite_number, f)
    else:
        print(f"I know your favorite number! This {filename}.")

numbers_user()















