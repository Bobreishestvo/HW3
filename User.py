"""
Пользователь - имеет логин и пароль, а так же календарь.
у пользователя есть итендифекатор начинающийся с @
"""


class User:
    def __init__(self, name, password, u_id):
        """ID пользовотеля используется в календаре для определения принадлежности"""
        self._name = name
        self._password = password
        self._id = u_id

    def __str__(self):
        return f"User {self._name} with ID {self._id} loaded"
