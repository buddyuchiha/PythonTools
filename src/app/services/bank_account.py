from app.utils.exceptions import (
    AccountBlockedError,
    BalanceLimitExceededError,
    BalanceLimitReducedError,
    InsufficientFundsError,
    NegativeAmountError,
    TooSmallTransactionError,
    TransactionLimitError
)


class BankAcount:
    __slots__ = (
        '__balance',
        '__max_balance',
        '__max_transaction',
        '__min_transaction',
        '__is_blocked' 
        )
    def __init__(
            self,
            balance: int, 
            max_balance: int = 1000000,
            max_transaction: int = 50000,
            min_transaction: int = 10, 
            is_blocked: bool = False 
        ) -> None:
        self.__balance = balance
        self.__max_balance = max_balance
        self.__max_transaction = max_transaction
        self.__min_transaction = min_transaction
        self.__is_blocked = is_blocked
        self.validate_balance()

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

    def deposit(self, amount: int) -> None:
        self.validate_deposit(amount)

        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        self.validate_withdraw(amount)
        
        self.__balance -= amount

    def get_balance(self) -> int:
        return self.__balance
    
    def block_account(self) -> None:
        self.__is_blocked = True

    def unblock_account(self) -> None:
        self.__is_blocked = False