from app.services.bank_account import BankAcount


if __name__ == "__main__":
    account = BankAcount(0)
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