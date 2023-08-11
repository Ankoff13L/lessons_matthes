

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


class User:

    def __init__(self, first_name, last_name, age):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age

    def describe_user(self):
        print(f"User: {self.f_name.title()} {self.l_name.title()}, {self.age} age. ")

    def greet_user(self):
        print(f"Hello {self.f_name.title()}!")

user_1 = User('anwei', 'smit', 31)
user_1.describe_user()
user_1.greet_user()




