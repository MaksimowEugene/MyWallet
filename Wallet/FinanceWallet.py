from Wallet.Transaction import Transaction
import json
import datetime


class FinanceWallet:
    """
    Класс FinanceWallet представляет личный финансовый кошелек.

    Атрибуты:
        filename (str): Имя файла для хранения данных о транзакциях.
        transactions (list): Список транзакций.
    """

    def __init__(self, filename='wallet.json'):
        """
        Создает новый объект FinanceWallet.

        Args:
            filename (str): имя файла для хранения данных о транзакциях.
        """
        self.filename = filename
        self.transactions = []
        self.read_transactions()

    def read_transactions(self):
        """
        Читает транзакции из файла и загружает их в список транзакций.
        """
        try:
            with open(self.filename, 'r') as file:
                transactions_raw = json.load(file)
            self.transactions = [Transaction(**trans) for trans in transactions_raw]
        except FileNotFoundError:
            self.transactions = []

    def save_transactions(self):
        """
        Сохраняет текущие транзакции в файл.
        """
        with open(self.filename, 'w') as file:
            json.dump([trans.to_dict() for trans in self.transactions], file, indent=4)

    def add_transaction(self, category, amount, description):
        """
        Добавляет новую транзакцию в кошелек.

        Args:
            category (str): категория транзакции.
            amount (float): сумма транзакции.
            description (str): описание транзакции.
        """
        today_date = datetime.datetime.now().date().strftime('%Y-%m-%d')
        transaction = Transaction(today_date, category, amount, description)
        self.transactions.append(transaction)
        self.save_transactions()

    def get_balance(self):
        """
        Вычисляет текущий баланс кошелька.

        Returns:
            tuple: кортеж, содержащий текущий баланс, доходы и расходы.
        """
        income = sum(trans.amount for trans in self.transactions if trans.category.lower() == 'доход')
        expense = sum(trans.amount for trans in self.transactions if trans.category.lower() == 'расход')
        return income - expense, income, expense

    def show_transactions(self):
        """
        Выводит все транзакции в кошельке.
        """
        for transaction in self.transactions:
            print(transaction)

    def edit_transaction(self, date, description):
        """
        Редактирует существующую транзакцию.

        Args:
            date (str): дата транзакции для редактирования.
            description (str): описание транзакции для редактирования.
        """
        for trans in self.transactions:
            if trans.date == date and trans.description == description:
                print(f"Текущая запись: {trans}")
                new_category = input("Введите новую категорию (оставьте пустым для сохранения текущей): ")
                new_amount = input("Введите новую сумму (оставьте пустым для сохранения текущей): ")
                new_description = input("Введите новое описание (оставьте пустым для сохранения текущего): ")

                if new_category:
                    trans.category = new_category
                if new_amount:
                    trans.amount = float(new_amount)
                if new_description:
                    trans.description = new_description

                self.save_transactions()
                print("Запись успешно обновлена.")
                return
        print("Запись не найдена.")

    def delete_transaction(self, date, description):
        """
        Удаляет существующую транзакцию.

        Args:
            date (str): дата транзакции для удаления.
            description (str): описание транзакции для удаления.
        """
        for trans in self.transactions:
            if trans.date == date and trans.description == description:
                self.transactions.remove(trans)
                self.save_transactions()
                print("Запись успешно удалена.")
                return
        print("Запись не найдена.")

    def search_transactions(self, search_query):
        """
        Выполняет поиск транзакций по запросу.

        Args:
            search_query (str): Строка для поиска.

        Returns:
            list: Список найденных транзакций.
        """
        found_transactions = [
            trans for trans in self.transactions
            if search_query.lower() in trans.date or
               search_query.lower() in trans.category.lower() or
               search_query in str(trans.amount) or
               search_query.lower() in trans.description.lower()
        ]
        if found_transactions:
            for trans in found_transactions:
                print(trans)
        else:
            print("Не найдено записей по запросу.")
