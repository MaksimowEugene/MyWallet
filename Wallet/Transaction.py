class Transaction:
    """
    Класс Transaction представляет отдельную финансовую транзакцию.

    Атрибуты:
        date (str): Дата транзакции в формате YYYY-MM-DD.
        category (str): Категория транзакции (доход или расход).
        amount (float): Сумма транзакции.
        description (str): Описание транзакции.
    """

    def __init__(self, date, category, amount, description):
        """
        Создает новый объект Transaction.

        Args:
            date (str): Дата транзакции.
            category (str): Категория транзакции.
            amount (float): Сумма транзакции.
            description (str): Описание транзакции.
        """
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        """
        Возвращает строковое представление транзакции.

        Returns:
            str: Строковое представление транзакции.
        """
        return f"Дата: {self.date}\nКатегория: {self.category}\nСумма: {self.amount}\nОписание: {self.description}\n"

    def to_dict(self):
        return {
            'date': self.date,
            'category': self.category,
            'amount': self.amount,
            'description': self.description
        }
