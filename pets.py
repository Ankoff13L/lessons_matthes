

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)





# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.pop('cat')

# print(pets)



# Позиционные аргументы
# def describe_pet(animal_type, pet_name):
#     """Выводит информацию о животном."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}' s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')


# # Именованые аргументы
# def describe_pet(animal_type, pet_name):
#     """Выводит информацию о животном."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}' s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster', pet_name='harry')


# Позиционные аргументы и применение значения по умолчанию
def describe_pet(pet_name, animal_type='dog'):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}' s name is {pet_name.title()}.")


describe_pet(pet_name='willie')

describe_pet(pet_name='harry', animal_type='hamster')

# describe_pet()








