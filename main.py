from Wallet.FinanceWallet import FinanceWallet


def menu():
    """
    Основное меню программы.
    """
    wallet = FinanceWallet()

    while True:
        print("\nЛичный финансовый кошелек")
        print("1. Показать баланс")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск по записям")
        print("5. Показать все транзакции")
        print("6. Выход")
        choice = input("\nВыберите действие: ")

        if choice == '1':
            balance, income, expense = wallet.get_balance()
            print(f"Текущий баланс: {balance} руб.")
            print(f"Доходы: {income} руб.")
            print(f"Расходы: {expense} руб.")
        elif choice == '2':
            category = input("Введите категорию (Доход/Расход): ")
            amount = float(input("Введите сумму: "))
            description = input("Введите описание: ")
            wallet.add_transaction(category, amount, description)
            print("Запись добавлена успешно.")
        elif choice == '3':
            date = input("Введите дату записи для редактирования (YYYY-MM-DD): ")
            description = input("Введите описание записи для редактирования: ")
            wallet.edit_transaction(date, description)
        elif choice == '4':
            query = input("Введите запрос для поиска (дата/категория/сумма/описание): ")
            wallet.search_transactions(query)
        elif choice == '5':
            wallet.show_transactions()
        elif choice == '6':
            break


if __name__ == "__main__":
    menu()
