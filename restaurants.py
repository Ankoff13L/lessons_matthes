

# class Restaurant():

#     def __init__(self, restaurant_name, cuisine_type):
#         self.rest_name = restaurant_name
#         self.cuisi_type = cuisine_type

#     def describe_restaurant(self):
#         print("\nIt's a trendy restaurant.")
#         print("You can have a delicious meal there.")

#     def open_restaurant(self):
#         print('Restaurant Open!')


# restaurant = Restaurant('brazier', 'fish')
# print(f"The restaurant is called {restaurant.rest_name.title()}!")
# print(f"This is a {restaurant.cuisi_type} restaurant.")

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant = Restaurant('brazier', 'fish')
# restaurant.describe_restaurant()

# restaurant = Restaurant('chili', 'vegan')
# restaurant.describe_restaurant()

# restaurant = Restaurant('hoof in the face', 'meat')
# restaurant.describe_restaurant()


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




# class Restaurant():

#     def __init__(self, restaurant_name, cuisine_type):
#         self.rest_name = restaurant_name
#         self.cuisi_type = cuisine_type
#         self.number_served = 0

#     def set_number_served(self, num_served):
#         """Позваляет задать количество обслуженных посетителей."""
#         self.number_served = num_served

#     def number_visitors(self):
#         """Выводит количество посетителей"""
#         print(f"\n{self.number_served} visitors served in total.")

#     def increment_number_served(self, number):
#         """Увеличивает количество обслуженных посетителей."""
#         self.number_served += number

#     def describe_restaurant(self):
#         print("\nIt's a trendy restaurant.")
#         print("You can have a delicious meal there.")

#     def open_restaurant(self):
#         print('Restaurant Open!')


# restaurant = Restaurant('brazier', 'fish')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant.set_number_served(5)
# restaurant.number_visitors()

# restaurant.increment_number_served (20)
# restaurant.number_visitors()






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

user_1 = User('anwei', 'smit', 31)
user_1.increment_login_attemps()
user_1.increment_login_attemps()
user_1.increment_login_attemps()
user_1.number_attemps()

user_1.reset_login_attemps()
user_1.number_attemps()


