"""Создание классов Privilegaes и Admin"""

from admin_user import User


class Privileges():
    def __init__(self):
        self.privileges = [
            'разрешено добавлять сообщения',
            'разрешено удалять пользователей',
            'разрешено банить пользователей',
        ]


    def show_privileges(self):
        """Выводит набор привелегий админа."""
        for privileg in self.privileges:
            print(privileg)


# admin_privileges = Privileges()
# admin_privileges.show_privileges()



class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges() # создал экземпляр класса Privileges как атрибут
                                        # класса Admin

