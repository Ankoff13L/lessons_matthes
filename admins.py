


# class User():

#     def __init__(self, first_name, last_name, age):
#         self.f_name = first_name
#         self.l_name = last_name
#         self.age = age

#     def describe_user(self):
#         print(f"User: {self.f_name.title()} {self.l_name.title()}, {self.age} age. ")

#     def greet_user(self):
#         print(f"Hello {self.f_name.title()}!")

# user_1 = User('anwei', 'smit', 31)
# user_1.describe_user()
# user_1.greet_user()



# class User():

#     def __init__(self, first_name, last_name, age):
#         self.f_name = first_name
#         self.l_name = last_name
#         self.age = age
#         self.login_attemps = 0


#     def describe_user(self):
#         print(f"User: {self.f_name.title()} {self.l_name.title()}, {self.age} age. ")

#     def greet_user(self):
#         print(f"Hello {self.f_name.title()}!")

#     def increment_login_attemps(self):
#         """Увеличивает попытки входа на 1."""
#         self.login_attemps += 1

#     def reset_login_attemps(self):
#         """Обнуляет значение попыток входа (login_attemps)"""
#         self.login_attemps -= self.login_attemps

#     def number_attemps(self):
#         """Сколько раз входили"""
#         print(f"Number of entries in the program: {self.login_attemps}.")



# user_1 = User('anwei', 'smit', 31)
# user_1.describe_user()
# user_1.greet_user()

# user_1 = User('anwei', 'smit', 31)
# user_1.increment_login_attemps()
# user_1.increment_login_attemps()
# user_1.increment_login_attemps()
# user_1.number_attemps()

# user_1.reset_login_attemps()
# user_1.number_attemps()





# class Admin(User):
#     def __init__(self, first_name, last_name, age):
#         super().__init__(first_name, last_name, age)
#         self.privileges = [
#             'разрешено добавлять сообщения',
#             'разрешено удалять пользователей',
#             'разрешено банить пользователей',
#         ]


#     def show_privileges(self):
#         """Выводит набор привелегий админа."""
#         for privileg in self.privileges:
#             print(privileg)

# my_admin = Admin('anwei', 'smit', 31)
# my_admin.show_privileges()





# class User():

#     def __init__(self, first_name, last_name, age):
#         self.f_name = first_name
#         self.l_name = last_name
#         self.age = age
#         self.login_attemps = 0


#     def describe_user(self):
#         print(f"User: {self.f_name.title()} {self.l_name.title()}, {self.age} age. ")

#     def greet_user(self):
#         print(f"Hello {self.f_name.title()}!")

#     def increment_login_attemps(self):
#         """Увеличивает попытки входа на 1."""
#         self.login_attemps += 1

#     def reset_login_attemps(self):
#         """Обнуляет значение попыток входа (login_attemps)"""
#         self.login_attemps -= self.login_attemps

#     def number_attemps(self):
#         """Сколько раз входили"""
#         print(f"Number of entries in the program: {self.login_attemps}.")


# # user_1 = User('anwei', 'smit', 31)
# # user_1.describe_user()
# # user_1.greet_user()



# class Privileges():
#     def __init__(self):
#         self.privileges = [
#             'разрешено добавлять сообщения',
#             'разрешено удалять пользователей',
#             'разрешено банить пользователей',
#         ]


#     def show_privileges(self):
#         """Выводит набор привелегий админа."""
#         for privileg in self.privileges:
#             print(privileg)


# # admin_privileges = Privileges()
# # admin_privileges.show_privileges()



# class Admin(User):
#     def __init__(self, first_name, last_name, age):
#         super().__init__(first_name, last_name, age)
#         self.privileges = Privileges() # создал экземпляр класса Privileges как атрибут
#                                         # класса Admin


# my_admin = Admin('anwei', 'smit', 31)
# my_admin.privileges.show_privileges()



"""Создание классов User, Privileges, Admin"""

class User():

    def __init__(self, first_name, last_name, age):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.login_attemps = 0


    def describe_user(self):
        print(f"User: {self.f_name.title()} {self.l_name.title()}, {self.age} age. ")

    def greet_user(self):
        print(f"Hello {self.f_name.title()}!")

    def increment_login_attemps(self):
        """Увеличивает попытки входа на 1."""
        self.login_attemps += 1

    def reset_login_attemps(self):
        """Обнуляет значение попыток входа (login_attemps)"""
        self.login_attemps -= self.login_attemps

    def number_attemps(self):
        """Сколько раз входили"""
        print(f"Number of entries in the program: {self.login_attemps}.")


# user_1 = User('anwei', 'smit', 31)
# user_1.describe_user()
# user_1.greet_user()



# class Privileges():
#     def __init__(self):
#         self.privileges = [
#             'разрешено добавлять сообщения',
#             'разрешено удалять пользователей',
#             'разрешено банить пользователей',
#         ]


#     def show_privileges(self):
#         """Выводит набор привелегий админа."""
#         for privileg in self.privileges:
#             print(privileg)


# admin_privileges = Privileges()
# admin_privileges.show_privileges()



class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges() # создал экземпляр класса Privileges как атрибут
                                        # класса Admin


my_admin = Admin('anwei', 'smit', 31)
my_admin.privileges.show_privileges()




