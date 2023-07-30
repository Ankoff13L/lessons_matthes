

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# print('........')
# print(current_number)


# current_number = 1
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)


# x = 1
# while x <=5:
#     print(x)



# available_toppings = ['mushrooms', 'olives', 'green peppers',
#                       'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry, we don't have {requested_topping}.")
# print("\nFinished making your pizza!")


# prompt = "\nList the toppings you want to add to the pizza: "
# prompt += "\nWhen you're done, enter 'quit': "

# while True:
#     message = input(prompt)

#     if message == 'quit':
#         break
#     else:
#         print("This topping is included in the order!")



# ages = "\nEnter your age: "
# ages += "\nWant to go out press 'quit': "


# while True:
#     age = input(ages)
#     if age == 'quit':
#         break
#     else:
#         age = int(age)
#         if age < 3:
#             price = 0
#         elif age == 3:
#             price = 10
#         elif age < 12:
#             price = 10
#         else:
#             price = 15

#         print(f"Your ticket is worth: ${price}.")



prompt = "\nList 3 toppings you would like to add to your pizza: "
prompt += "\nWhen you're done, enter 'quit': "

active = True
current_number = 0
while active:
    message = input(prompt)
    current_number += 1

    if message == 'quit':
        break
    elif current_number == 3:
        active = False
    else:
        print("This topping is included in the order!")

