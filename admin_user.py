"""Создание класса User"""

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

