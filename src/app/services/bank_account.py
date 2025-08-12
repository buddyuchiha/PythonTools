from app.utils.exceptions import (
    AccountBlockedError,
    BalanceLimitExceededError,
    BalanceLimitReducedError,
    InsufficientFundsError,
    NegativeAmountError,
    TooSmallTransactionError,
    TransactionLimitError,
    TransactionListLengthError
)
from app.utils.logging import logger
from core.config import config

class BankAccount:
    __slots__ = (
        '__balance',
        '__max_balance',
        '__max_transaction',
        '__min_transaction',
        '__max_history_length',
        '__is_blocked',
        '__transictions_history'
        )
    def __init__(
            self,
            balance: int, 
            max_balance: int = 1000000,
            max_transaction: int = 50000,
            min_transaction: int = 10, 
            max_history_length: int = 1000,
            is_blocked: bool = False 
        ) -> None | Exception:  
        self.__balance = balance
        self.__max_balance = max_balance
        self.validate_balance()
        
        self.__max_transaction = max_transaction
        self.__min_transaction = min_transaction
        self.__max_history_length = max_history_length
        self.__is_blocked = is_blocked
        
        self.__transictions_history = list()

        logger.info(
            f"Created account with balance = {self.__balance}"
            )

    def validate_balance(self) -> None | Exception:
        if self.__balance > self.__max_balance:
            raise BalanceLimitExceededError
        
        if self.__balance < 0:
            raise BalanceLimitReducedError
        
    def validate_amount(self, amount: int) -> None | Exception:
        if amount < 0:
            raise NegativeAmountError
        
        if amount > self.__max_transaction:
            raise TransactionLimitError
        
        if amount < self.__min_transaction:
            raise TooSmallTransactionError

    def validate_account(self) -> None | Exception:
        if self.__is_blocked == True:
            raise AccountBlockedError

    def validate_default_operation(self, amount: int) -> None | Exception:
        self.validate_balance()
        self.validate_account()
        self.validate_amount(amount)

    def validate_deposit(self, amount: int) -> None | Exception:
        self.validate_default_operation(amount)

        if self.__balance + amount > self.__max_balance:
            raise BalanceLimitExceededError

    def validate_withdraw(self, amount: int) -> None | Exception:
        self.validate_default_operation(amount)
        
        if self.__balance - amount < 0:
            raise InsufficientFundsError

    def write_transaction(self, operation: str, amount: int) -> None:
        if len(self.__transictions_history) <= self.__max_history_length:
            self.__transictions_history.append(
                {
                    "operation" : operation,
                    "amount"    : amount,
                    "balance"   : self.__balance
                }
            )
        else:
            raise TransactionListLengthError

    def deposit(self, amount: int) -> None:
        self.validate_deposit(amount)

        self.__balance += amount

        logger.info(
            f"Deposite maded"
            )
        
        self.write_transaction("withdraw", amount)


    def withdraw(self, amount: int) -> None:
        self.validate_withdraw(amount)
        
        self.__balance -= amount

        logger.info(
            f"Withdraw maded"
            )
        
        self.write_transaction("withdraw", amount)

    def get_balance(self) -> int:
        self.validate_balance()

        return self.__balance
    
    def get_transaction_history(self) -> list[dict]:
        return self.__transictions_history
    
    def save_history_to_file(self) -> None:
        with open(config["PATH"]["TRANSACTIONS"], "w") as file:
            for transaction in self.__transictions_history:
                file.write(str(transaction))
                file.write("\n")
        
        logger.info("History saved")

    def block_account(self) -> None:
        self.__is_blocked = True

        logger.info("Account blocked")

    def unblock_account(self) -> None:
        self.__is_blocked = False

        self.validate_account()

        logger.info("Account unblocked")
