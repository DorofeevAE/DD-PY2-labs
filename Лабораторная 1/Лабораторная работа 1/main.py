# TODO Написать 3 класса с документацией и аннотацией типов
class Student:
    """
    Документация на класс. Класс описывает полученную студентом оценку
    """
    def __init__(self, name: str, surname: str, grade: int):
        """
        Инициалзация экземпляра класса.
        :param name: имя студента
        :param surname: фамилия студента
        :param grade: оценка студента
        """
        self.name = name
        self.surname = surname
        if not isinstance(name and surname, str):
            raise TypeError("""Имя и фамилия должны быть списком """)
        self.grade = grade
        if 5 < grade < 2:
            raise ValueError("""Оценка должна принимать значение от 2 до 5 """)

    def change_grade(self, new_grade: int):
        ...
    """
    Метод изменяет оценку студента.
    :param new_grade: новая оценка студента.
    """
    def check_attestation(self) -> bool:
        ...
    """
    :return: аттестован ли студент.
    """


class Chair:
    """
    Документация на класс. Класс описывает стул
    """
    def __init__(self, material: str, color: str):
        """
        Инициалзация экземпляра класса.
        :param material: материал стула
        :color: цвет стула
        """
        self.material = material
        self.color = color
        if not isinstance(material and color, str):
            raise TypeError("""Цвет и материал должны быть списком """)

    def check_price(self, price: int):
        ...
    """
    Метод проверяет стоимость стула с определенными атрибутами.
    :param price: стоимость стула.
    """
    def change_color(self, new_color: str):
        ...
    """
    Метод изменяет цвет стула.
    :param new_color: новый цвет стула.
    """


class Text:
    """
    Документация на класс. Класс описывает текст
    """
    def __init__(self, pages: int, symbols: int):
        """
        Инициалзация экземпляра класса.
        :param pages: количество страниц в тексте,
        :param symbols: количество символов в тексте
        """
        self.pages = pages
        self.symbols = symbols
        if not isinstance(pages and symbols, int):
            raise TypeError("""Количество страниц и символов в тексте - целое число """)
        if symbols and pages < 0:
            raise ValueError("""Количество страниц и символов не должно быть отрицательным """)

    def increment_last_read_page(self, read_pages: int):
        ...
    """
    Метод увеличивает номер последней прочитанной страницы.
    :param read_pages: количество прочитанных страниц
    """
    def translate_text(self, language):
        ...
    """
    Метод переводит текст на другой язык.
    :param language: язык, на который необходимо перевести текст
    """


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
