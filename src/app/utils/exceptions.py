from app.utils.logging import logger

class BankException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InsufficientFundsError(BankException):
    def __init__(
            self,
            message: str = "Don't enough money for withdraw"
            ) -> None:
        logger.error("InsufficientFundsError")

        super().__init__(message)


class NegativeAmountError(BankException):
    def __init__(
            self, 
            message: str = "Attempt to make operation with negative amount"
            ) -> None:        
        logger.error("NegativeAmountError")

        super().__init__(message)


class AccountBlockedError(BankException):
    def __init__(self, message: str = "Account is blocked") -> None:
        logger.error("AccountBlockedError")
        
        super().__init__(message)

    
class BalanceLimitExceededError(BankException):
    def __init__(
            self,
            message: str = "Exceeding the balance limit"
            ) -> None:
        logger.error("BalanceLimitExceededError")

        super().__init__(message)


class BalanceLimitReducedError(BankException):
    def __init__(
            self,
            message: str = "Reducing the balance limit"
            ) -> None:
        logger.error("BalanceLimitReducedError")
        
        super().__init__(message)

    
class TransactionLimitError(BankException):
    def __init__(
            self, message: str = "Exceeding the operation limit"
            ) -> None:
        logger.error("TransactionLimitError")

        super().__init__(message)


class TooSmallTransactionError(BankException):
    def __init__(
            self,
            message: str = "Amount is less than the minimum limit"
            ) -> None:
        logger.error("TooSmallTransactionError  ")

        super().__init__(message)


class TransactionListLengthError(BankException):
    def __init__(
            self,
            message: str = "Transaction List overflow"
            ) -> None:
        logger.error("TransactionListLengthError")

        super().__init__(message)