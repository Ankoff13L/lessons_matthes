

# prompt = "If you tell us who you are, we can personalize the messages you sww."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(F"\n Hello, {name}!")



# height = input("\nHow tall are you, in inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're little older.")




# def greet_user():
#     """Выводит простое приветствие."""
#     print('Hello!')

# greet_user()



# def greet_user(username):
#     """Выводит простое приветствие."""
#     print(f"Hello, {username.title()}!")

# greet_user('jesse')
# greet_user('sarah')



# """Простоая версия get_formatted_name() с бесконечным циклом"""
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# # Бесконечный цикл
# while True:
#     print("\nPleese tell me your name: ")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formated_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formated_name}!")



# """Простоая версия get_formatted_name() с бесконечным циклом"""
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# # Бесконечный цикл
# while True:
#     print("\nPleese tell me your name: ")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formated_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formated_name}!")


"""Доработанная версия get_formatted_name() с выходм из бесконечного цикла"""
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPleese tell me your name: ")
    print("(enter 'q' at any time to quit)")   # добавили

    f_name = input("First name: ")
    if f_name == 'q':                          # добавили
        break                                  # добавили

    l_name = input("Last name: ")
    if f_name == 'q':                          # добавили
        break                                  # добавили


    formated_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formated_name}!")


