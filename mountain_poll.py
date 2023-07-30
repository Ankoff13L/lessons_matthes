# responses = {}
# # Установка флага продолжения опроса.
# polling_active = True

# while polling_active:
#      # Запрос имени и ответа пользователя.
#      name = input("\nWhat is your name? ")
#      response = input("Which mountain would you like to climb someday? ")

#      # Ответ сохраняется в словаре:
#      responses[name] = response

#      # Проверка продолжения опроса.
#      repeat = input("Would you like to let another person respond? (yes/ no) ")
#      if repeat == 'no':
#         polling_active = False

#  # Опрос завершен, вывести результаты.
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")


# sandwich_orders = ['tuna', 'pastrami', 'avokado', 'steak & cheese', 'pastrami', 'chiken', 'pastrami']
# finished_sandwiches = []

# while sandwich_orders:
#     sandwich_order = sandwich_orders.pop()
#     print(f"I made your {sandwich_order} sandwich.")
#     finished_sandwiches.append(sandwich_order)

# print('\nThe following Sandichi with:')
# for orders in finished_sandwiches:
#     print(f"\n{orders}")



# sandwich_orders = ['tuna', 'pastrami', 'avokado', 'steak & cheese', 'pastrami', 'chiken', 'pastrami']
# finished_sandwiches = []


# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print ('Dear guests of the Pastens are over.')


# while sandwich_orders:
#     sandwich_order = sandwich_orders.pop()
#     print(f"I made your {sandwich_order} sandwich.")
#     finished_sandwiches.append(sandwich_order)

# print('\nThe following Sandichi with:')
# for orders in finished_sandwiches:
#     print(f"{orders}")


resting_place = {}

active = True
while active:
    names = input('\nHello, how your name? ')
    vacations = input('Where would you like to spend your vacation? ')

    resting_place[names] = vacations
    repeat = input('You want to continue? "yes" or "no" ')
    if repeat == 'n':
        active = False



print('\nWho and where wants to spend a vacation:')
for name, vacation in resting_place.items():
    print(f'{name.title()}: {vacation.title()}')



