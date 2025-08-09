class BankException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InsufficientFundsError(BankException):
    def __init__(
            self,
            message: str = "Don't enough money for withdraw"
            ) -> None:
        super().__init__(message)


class NegativeAmountError(BankException):
    def __init__(
            self, 
            message: str = "Attempt to make operation with negative amount"
            ) -> None:
        super().__init__(message)


class AccountBlockedError(BankException):
    def __init__(self, message: str = "Account is blocked") -> None:
        super().__init__(message)

    
class BalanceLimitExceededError(BankException):
    def __init__(
            self,
            message: str = "Exceeding the balance limit"
            ) -> None:
        super().__init__(message)


class BalanceLimitReducedError(BankException):
    def __init__(
            self,
            message: str = "Reducing the balance limit"
            ) -> None:
        super().__init__(message)

    
class TransactionLimitError(BankException):
    def __init__(
            self, message: str = "Exceeding the operation limit"
            ) -> None:
        super().__init__(message)


class TooSmallTransactionError(BankException):
    def __init__(
            self,
            message: str = "Reducing the balance limit"
            ) -> None:
        super().__init__(message)