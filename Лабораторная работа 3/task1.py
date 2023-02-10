class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        """Геттер возвращает защищенный атрибут _name"""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Сеттер присваивает новое значение защищенному атрибуту _name"""
        if not isinstance(new_name, str):
            raise TypeError("Имя книги должно быть типом str")
        self._name = new_name

    @property
    def author(self) -> str:
        """Геттер возвращает защищенный атрибуту _author"""
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        """Сеттер присваивает новое значение защищенному атрибуту _author"""
        if not isinstance(new_author, str):
            raise TypeError("Имя автора должно быть типом str")
        self._author = new_author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Страницы {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, {self.__class__.__author__} author={self.author!r}, " \
               f"pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError
        self._pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, {self.__class__.__author__} author={self.author!r}, " \
               f"duration={self.duration!r})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError
        if new_duration <= 0:
            raise ValueError
        self._duration = new_duration


print(Book("Азбука", "Морзе"))
