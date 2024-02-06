"""
Сущность, отвечающая за храние и предоставление данных
Оно хранит пользователей, календари и события.
Хранение в том числе означает сохранение между сессиями в csv файлах
(пароли пользователей хранятся как hash)

Должен быть статическим или Синглтоном

*) Нужно хранить для каждого пользователя все события которые с нима произошли но ещё не были обработаны.
"""
import csv
from User import User


class Backend:
    """Singletone"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            print("Backend started")
        else:
            print("Backend already exist")
        return cls._instance

    def __init__(self):
        self.passwords = ""
        self.current_user = ""
        print(f"Backend init success")

    def check_name(self):
        """Проверяем имя пользователя"""
        with open('users.csv', 'r') as p_file:
            csv_passwords = csv.reader(p_file, delimiter=";")
            header = True

            for row in csv_passwords:
                # print(row)
                if header is True:
                    header = False
                    continue

                Backend.passwords = row
                if self not in Backend.passwords[0]:
                    continue
                else:
                    return True
            return False

    def check_password(self, name):
        """Проверяем пароль пользователя"""
        print(self)
        if (self) == Backend.passwords[1]:
            Backend.current_user = User(Backend.passwords[0], Backend.passwords[1], Backend.passwords[2])
            return True
        else:
            return False

    def new_user(self, password):
        """Создаем нового пользователя"""
        with open("users.csv", mode="a") as p_file:
            file_writer = csv.writer(p_file, delimiter=";", lineterminator="\n")
            file_writer.writerow([self, password, "@" + str(self)])
        print(f'Пользователь {self} добавлен, необходим перезапуск')
