# import json

# username = input("What is your name? ")

# filename = 'username.json'
# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print(f"We'll remember you come back, {username}!")


# import json

# # Программа загружает имя пользователя, если оно было сохранено ранее.
# # В противном случает она запрашивает имя пользователя и сохраняет его.
# filename = 'username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f"We'll remember you come back, {username}!")
# else:
#     print(f"Welcome back, {username}")



# import json

# def greet_user():
#     """Приветствует пользователя по имени."""
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w') as f:
#             json.dump(username, f)
#             print(f"We'll remember you come back, {username}!")
#     else:
#         print(f"Welcome back, {username}")

# greet_user()


# import json

# def get_stored_username():
#     """Получает хранимое имя пользователя, если оно существует."""
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username

# def greet_user():
#     """Приветсвует пользователя по имени."""
#     username = get_stored_username()
#     if username:
#         print(f"Welcome back, {username}")
#     else:
#         username = input("What is your name? ")
#         filename = 'username.json'
#         with open(filename, 'w') as f:
#             json.dump(username, f)
#             print(f"We'll remember you come back, {username}!")
# greet_user()


# import json

# def get_stored_username():
#     """Получает хранимое имя пользователя, если оно существует."""
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username

# def get_new_username():
#     """Запрашивает новое имя пользователя."""
#     username = input("What is your name? ")
#     filename = 'username.json'
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#     return username

# def greet_user():
#     """Приветсвует пользователя по имени."""
#     username = get_stored_username()
#     if username:
#         print(f"Welcome back, {username}")
#     else:
#         username = get_new_username()
#         print(f"We'll remember you come back, {username}!")

# greet_user()



import json

def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Приветсвует пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}")

def check_usernames():
    """Проверяет имя последнего пользователя"""
    username = get_stored_username()
    check_username = input (f"Your name is {username}? \ny/n ")
    if check_username == 'y':
        greet_user()
    else:
        username = get_new_username()
        print(f"We'll remember you come back, {username}!")

check_usernames()



