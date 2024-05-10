import unittest
from Wallet.Transaction import Transaction


class TestTransaction(unittest.TestCase):

    def test_transaction_creation(self):
        # Проверка создания объекта Transaction
        transaction = Transaction("2024-05-07", "Доход", 100.0, "Зарплата")
        self.assertEqual(transaction.date, "2024-05-07")
        self.assertEqual(transaction.category, "Доход")
        self.assertEqual(transaction.amount, 100.0)
        self.assertEqual(transaction.description, "Зарплата")

    def test_string_representation(self):
        # Проверка строкового представления транзакции
        transaction = Transaction("2024-05-07", "Доход", 100.0, "Зарплата")
        expected_string = "Дата: 2024-05-07\nКатегория: Доход\nСумма: 100.0\nОписание: Зарплата\n"
        self.assertEqual(str(transaction), expected_string)


if __name__ == "__main__":
    unittest.main()
