
# name_users = ['djon', 'lisa', 'admin', 'ivan', 'anwei']

# for name_user in name_users:
#     if name_user == 'admin':
#         print('Hello admin, would yuo like to see a status report?')

#     else:
#         print(f'Hello {name_user.title()}, thank you for logging in again')


# name_users = ['jhon', 'lisa', 'admin', 'ivan', 'anwei']

# name_users = []

# if name_users:
#     for name_user in name_users:
#         if name_user == 'admin':
#             print('Hello admin, would yuo like to see a status report?')

#         else:
#             print(f'Hello {name_user.title()}, thank you for logging in again')
# else:
#     print('We need to ind some users!')

# Сверка списка имен зарегистрированных пользователей с новыми пользователями с учетом регистра
# т.е. если одно и тоже имя в обоих списках  будет записано с разным регистром это не будет 
# совпадением, например jhon и Jhon считаются разными именами

# current_users = ['john', 'lisa', 'admin', 'ivan', 'anwei'] # список зарег. пользователей
# new_users = ['billy', 'anna', 'admin', 'danila', 'anwei'] # список новых пользователей

# for new_user in new_users: # создаем цикл for 
#     if new_user in current_users: # благодаря ключевому слову in сравниваем два списка
#         print(f'The name {new_user.title()} is already in use. Choose a different name!') # текст когда есть совпадение
#     else:
#         print(f"You can choose the name {new_user.title()}!") # текст когда нет совпадения



# Сверка списка имен зарегистрированных пользователей с новыми пользователями без учета рагистра
# чтобы регистр не влиял на проверку: JOHN, John и john считаются совпадением имен

# current_users = ['john', 'lisa', 'admin', 'ivan', 'anwei'] # список зарег. пользователей
# new_users = ['billy', 'anna', 'admin', 'danila', 'anwei'] # список новых пользователей

# current_users_lower = [users.lower() for users in current_users] # создаем копию списка current_users
                                                                   # в которой все значения приводим
                                                                   # к нижнему регистру

# for new_user in new_users:
#     if new_user in current_users_lower: # благодаря ключевому слову in сравниваем два списка
#         print(f'The name {new_user.title()} is already in use. Choose a different name!') # текст когда есть совпадение
#     else:
#         print(f"You can choose the name {new_user.title()}!") # текст когда нет совпадения и имя региструется

# numbers = []
# numbers = list(range(1, 10))


# numbers = [number for number in range(1, 10)]
# print(numbers)

numbers = []
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f'{number}th')





