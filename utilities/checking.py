"""Методы для проверки наших запросов"""


class Cheking:

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print("Успешно!!! Статус код = " + str(result.status_code))
