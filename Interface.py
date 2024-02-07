"""
Позволяет зайти по логину-паролю или создать нового пользователя (а так же выйти из аккаунта)
Позволяет выбрать календарь, узнать ближайшие события, события из промежутка времени а так же
Создать событие или удалить событие
После создания события можно добавить туда пользователей
Если нас добавили в событие или удалили мы получаем уведомление.

в main можно использовать ТОЛЬКО interface
"""
import sys
from Backend import Backend
from Calendar import Calendar


class Interface:
    def __init__(self):
        name = ""
        password = ""
        print(f"Interface init success")

    @staticmethod
    def start():
        'запускаем бэкэнд'
        work_backend = Backend()
        Interface.identification(input("Введите имя пользователя?\n"))

    @staticmethod
    def exit_interface():
        print("Exiting the program...")
        sys.exit(0)

    def identification(self):
        "идентификация пользователя"
        if Backend.check_name(self) is True:
            Interface.name = self
            Interface.authentication(input("Введите пароль?\n"), Interface.name)
        else:
            print("Пользователь не найден")
            Interface.new_user(self)

    def authentication(self, name):
        "аутентификация пользователя"
        if Backend.check_password(self, name) is False:
            print("Пароль неверен")
        else:
            print(Backend.current_user)
            Interface.main_menu()
    @staticmethod
    def main_menu():
        '''Меню управления календарем'''
        print(f'''1. Выбор календаря\n2. Ближашее событие\n3. События в интервале\n4. Добавить новое событие\n5. Удалить событие
        Есть новые события if Calendar.check_new_notification() is True else нет новых событий''')

        command = int(input("Выберите команду (введите цифру):"))
        if command == 1:
            pass
        elif command == 2:
            pass
        elif command == 3:
            pass
        elif command == 4:
            pass
        elif command == 5:
            pass
        else:
            print("Ошибка ввода")

    def new_user(self):
        'создание нового пользователя'
        question = input(f'Создать нового пользователя {self}? (y/n)\n')
        if question == 'y':
            user_new = self
            password_new = input(f'Введите пароль для {self}\n')
            if len(password_new) != 0:
                Backend.new_user(user_new, password_new)
            else:
                print("Пароль не может быть пустым")
                Interface.exit_interface()
        elif question == 'n':
            Interface.exit_interface()
        else:
            print('Ввод не распознан')
            Interface.exit_interface()
