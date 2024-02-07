"""
Класс календаря - хранит события.
он умеет искать все события из промежутка (в том числе повторяющиеся)
он умеет добавлять/удалять события.
У каждого календаря ровно один пользователь.
"""


class Calendar:
    def __init__(self):
        self._notification = False
        self._events = []

    @staticmethod
    def new_notification():
        Calendar._notification = True
    @staticmethod
    def check_new_notification():
        if Calendar._notification is True:
            return True

