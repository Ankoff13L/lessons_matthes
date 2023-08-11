
class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):  # метод
        """Инициализирует атрибуты name и age."""
        self.name = name     # это переменная (атрибут) экземпляра
        self.age = age       # это переменная (атрибут) экземпляра

    def sit(self):
        """Собака садится по команде."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f"{self.name} rolled over!")


my_dog = Dog('willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} yers old.")
my_dog.sit()
my_dog.roll_over()


your_dog = Dog('lucy', 3)

print(f"\nMy dog's name is {your_dog.name}")
print(f"My dog is {your_dog.age} yers old.")
your_dog.sit()






