from enum import Enum


class ErrorCode(int, Enum):
    # customer 1xx
    CUSTOMER_NOT_FOUND = 100
    CUSTOMER_ALREADY_EXISTS = 101
    CUSTOMER_IS_NOT_AVAILABLE = 102
