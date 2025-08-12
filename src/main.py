from app.services.bank_account import BankAccount


if __name__ == "__main__":
    account = BankAccount(0)
    account.block_account()
    account.unblock_account()
    account.deposit(100)
    account.withdraw(20)
    account.withdraw(20)
    account.withdraw(20)
    account.withdraw(20)
    account.withdraw(20)
    account.deposit(10000)
    print(account.get_balance())
    print(account.get_transaction_history())
    account.save_history_to_file()
