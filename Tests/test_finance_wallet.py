import unittest
from Wallet.FinanceWallet import FinanceWallet


class TestFinanceWallet(unittest.TestCase):

    def setUp(self):
        # Создаем экземпляр кошелька для тестирования
        self.wallet = FinanceWallet(filename='test_wallet.json')

    def tearDown(self):
        # Удаляем временный файл после выполнения тестов
        self.wallet = None
        import os
        os.remove('test_wallet.json')

    def test_add_transaction(self):
        # Добавляем транзакцию
        self.wallet.add_transaction('доход', 100, 'Зарплата')
        # Проверяем, что транзакция добавлена
        self.assertEqual(len(self.wallet.transactions), 1)
        # Проверяем, что баланс правильный
        self.assertEqual(self.wallet.get_balance()[0], 100)

    def test_edit_transaction(self):
        # Добавляем транзакцию
        self.wallet.add_transaction('расход', 50, 'Покупка продуктов')
        # Редактируем транзакцию
        self.wallet.edit_transaction('2024-05-10', 'Покупка продуктов')
        # Проверяем, что описание транзакции изменилось
        self.assertEqual(self.wallet.transactions[0].description, 'Новое описание')

    def test_delete_transaction(self):
        # Добавляем транзакцию
        self.wallet.add_transaction('расход', 50, 'Покупка продуктов')
        # Удаляем транзакцию
        self.wallet.delete_transaction('2024-05-10', 'Покупка продуктов')
        # Проверяем, что транзакция удалена
        self.assertEqual(len(self.wallet.transactions), 0)

    def test_search_transactions(self):
        # Добавляем транзакцию
        self.wallet.add_transaction('расход', 50, 'Покупка продуктов')
        # Ищем транзакцию
        self.wallet.search_transactions('Покупка')
        # Проверяем, что найдена нужная транзакция
        self.assertEqual(len(self.wallet.transactions), 1)


if __name__ == '__main__':
    unittest.main()
