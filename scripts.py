class Scripts:
    """
    Класс для управления расходами, добавления, получения и очистки данных
    :param data: Словарь для хранения данных о расходах
    :param count: Счётчик расходов
    """

    def __init__(self):
        """
        Инициализация класса Scripts
        :param data: Словарь для хранения данных о расходах (по умолчанию пустой)
        :param count: Счётчик расходов (по умолчанию 0)
        :return: None
        """
        self.data = {}
        self.count = 0

    def add_expense(self, amount: float, category: str, description: str) -> None:
        """
        Добавить расход в список
        :param amount: Сумма расхода
        :param category: Категория расхода
        :param description: Описание расхода
        :return: None
        """
        self.data[f"{self.count}"] = (amount, category, description)
        self.count += 1

    def get_expenses(self) -> dict:
        """
        Получить все расходы
        :return: Словарь с расходами, где ключи — индексы, значения — кортежи (сумма, категория, описание)
        """
        return self.data

    def get_total(self) -> float:
        """
        Получить общую сумму расходов
        :return: Сумма всех расходов
        """
        return sum(value[0] for value in self.data.values())

    def get_by_category(self, category: str) -> list:
        """
        Получить расходы по категории
        :param category: Категория, по которой фильтруются расходы
        :return: Список кортежей, каждый из которых содержит (сумма, описание) для выбранной категории
        """
        return [(amount, desc) for amount, cat, desc in self.data.values() if cat == category]

    def clear_expenses(self) -> None:
        """
        Очистить все расходы (от себя решил)))
        :return: None
        """
        self.data = {}
        self.count = 0
