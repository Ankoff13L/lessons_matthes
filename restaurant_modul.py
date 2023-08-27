"""Создание ресторанов простого и с мороженным"""


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.rest_name = restaurant_name
        self.cuisi_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, num_served):
        """Позваляет задать количество обслуженных посетителей."""
        self.number_served = num_served

    def number_visitors(self):
        """Выводит количество посетителей"""
        print(f"\n{self.number_served} visitors served in total.")

    def increment_number_served(self, number):
        """Увеличивает количество обслуженных посетителей."""
        self.number_served += number

    def describe_restaurant(self):
        print("\nIt's a trendy restaurant.")
        print("You can have a delicious meal there.")

    def open_restaurant(self):
        print('Restaurant Open!')



class IceCreamStand(Restaurant):
    """Опрелеляется класс-потомок класса-родителя Restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []


    def flavors_name(self):
        """Выводит список вкусов мороженого."""
        print(self.flavors)





