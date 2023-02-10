if __name__ == "__main__":
    class Sport:
        """
        Базовый класс спорт.
        """
        def __init__(self, name: str, season: str, num_of_people: int):
            """ Инициализация экземпляра класса.
            :param name: Название спорта
            :param season: Время проведения
            :param num_of_people: количество спортсменов
            Примеры:
            >>> sport = Sport(tennis, summer, 2)
            """
            self.name = name
            self.season = season
            self.num_of_people = num_of_people

        def __str__(self):
            """ Реализация магического метода __str__"""
            return f"Спорт {self.name}. Время проведения {self.season}. Количество спортсменов {self.num_of_people} "

        def __repr__(self):
            """ Реализация магического метода __repr__"""
            return f"{self.__class__.name__}(name = {self.name!r}, {self.__class__.__season__} season = {self.author!r},num_of_people={self.num_of_people!r})"

        @property
        def name (self) -> str:
            return self._name

        @name.setter
        def name(self, name: str) -> None:
            if not isinstance(name, str):
                raise TypeError("Название вида спорта должно быть типа str")
            self._name = name

        @property
        def season(self) -> str:
            return self.season

        @season.setter
        def season(self, season: str) -> None:
            """Определяется время проведения спорта"""
            if not isinstance(season, str):
                raise TypeError("Время проведения должно быть типом str")
            self._season = season

        @property
        def num_of_people(self) -> str:
            return self._num_of_people

        @num_of_people.setter
        def num_of_people(self, num_of_people: int) -> None:
            """Определяется количество людей"""
            if not isinstance(num_of_people, int):
                raise TypeError("Количество спортсменов должно быть типом int")
            if num_of_people <= 0:
                raise ValueError("Число спортсменов должно быть положительным")
            self._num_of_people = num_of_people

    class SkiRace(Sport):
        """Дочерний класс
        :param equipment: Инвентарь
        """
        def __int__(self, name: str, season: str, num_of_people: int, equipment: str):
            """Вызов конструктора базового класса"""
            super().__init__(name)
            super().__init__(season)
            super().__init__(num_of_people)
            self.equipment = equipment

        def __repr__(self):
            return f"{self.__class__.name__}(name = {self.name!r}, {self.__class__.__season__} season = {self.season!r},num_of_people={self.num_of_people!r}, equipment = {self.equipment!r})"

        @property
        def equipment(self) -> str:
            return self._equipment

        @equipment.setter
        def equipment(self, equipment: str):
            """Определяется необходимый инвентарь"""
            if not isinstance(equipment, str):
                raise TypeError("Инвентарь должен быть типом str")
            self._equipment = equipment

    class Volleyball(Sport):
        """Дочерний класс
        :param num_of_periods: Количество периодов в игре
        """
        def __int__(self, name: str, season: str, num_of_people: int, num_of_periods: int):
            """Вызов конструктора базового класса"""
            super().__init__(name)
            super().__init__(season)
            super().__init__(num_of_people)
            self.num_of_periods = num_of_periods

        def __repr__(self):
            return f"{self.__class__.name__}(name = {self.name!r}, {self.__class__.__season__} season = {self.season!r},num_of_people={self.num_of_people!r}, num_of_periods = {self.num_of_periods!r})"

        @property
        def num_of_periods(self) -> int:
            return self._num_of_periods

        @num_of_periods.setter
        def num_of_periods(self, num_of_periods:int):
            """Определяется число периодов"""
            if not isinstance(num_of_periods, int):
                raise TypeError
            if num_of_periods <= 0:
                raise ValueError
            self._num_of_periods = num_of_periods
    pass
