
# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings: 
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings: 
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings: 
#         print("Adding extra cheese.")

# print("\nFinished making your pizza!")

# alien_color = ['green', 'yellow', 'red']

# if 'green' in alien_color:
#     number = 5
# elif 'yellow'in alien_color:
#     number = 10
# elif 'red'in alien_color:
#     number = 15


# print(f"\nThe player has just earned {number} points")

# if 'black' in alien_color:
#     number = 5
# elif 'yellow'in alien_color:
#     number = 10
# elif 'red'in alien_color:
#     number = 15


# print(f"\nThe player has just earned {number} points")

# if 'black' in alien_color:
#     number = 5
# elif 'gray'in alien_color:
#     number = 10
# elif 'red'in alien_color:
#     number = 15


# print(f"\nThe player has just earned {number} points")

# age = 65

# if age < 2:
#     life_period = 'baby'
# elif age < 4:
#     life_period = 'Baby'
# elif age < 13:
#     life_period = 'child'
# elif age < 20:
#     life_period = 'teenager'
# elif age < 65:
#     life_period = 'adult'
# elif age >= 65:
#     life_period = 'old man'

# print(f'You are a {life_period}!')


# favorite_fruits = ['apples', 'bananas', 'melons', 'pears', 'peaches']

# if 'apples' in favorite_fruits:
#     print('You have apples')
# if 'bananas' in favorite_fruits:
#     print('You have bananos')
# if 'pineapple' in favorite_fruits:
#     print('You have pineapple')
# if 'pears' in favorite_fruits:
#     print('You have pears')


# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza!")


# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print('Ssori, we are out of green peppers right now. ')
#     else:
#         print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza!")




# requested_toppings = []

# if requested_toppings: 
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")

#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")


available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

