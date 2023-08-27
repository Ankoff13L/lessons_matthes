"""Набор класов для представления электромобимлей."""

class Battery():
    """Простая модель аккумулятора автомобиля."""


    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size


    def upgrade_battery(self):
        """
        Проверяет размер аккумулятора и устанавливает мощность равной 100,
        если он имеет другое значение.
        """
        if self.battery_size < 100:
            self.battery_size = 100

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        """Выводит приблизительный запас ходя для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} milles on a full charge.")




class ElectricCar(Car):
    """
    Инициализирует атрибуты класса-родителя.
    Затем инициализирует атрибуты, специфические для электромобиля.
    """

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        self.battery = Battery()





