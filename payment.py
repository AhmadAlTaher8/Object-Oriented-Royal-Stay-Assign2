"""
payment.py
Defines the Payment base class for the hotel management system.
"""

class Payment:
    """
    The Payment class is a base class for handling different payment methods.
    """

    def __init__(self, payment_id: int, amount: float, method: str):
        """
        Initializes a new Payment object.

        :param payment_id: Unique ID for the payment.
        :param amount: The total amount to be paid.
        :param method: The payment method (e.g., "Credit Card", "Cash").
        """
        self.__payment_id = payment_id
        self.__amount = amount
        self.__method = method

    def process_payment(self) -> bool:
        """
        Processes the payment. This method is intended to be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    # Getters and Setters
    def get_payment_id(self) -> int:
        return self.__payment_id

    def get_amount(self) -> float:
        return self.__amount

    def set_amount(self, new_amount: float) -> None:
        self.__amount = new_amount

    def get_method(self) -> str:
        return self.__method

    def set_method(self, new_method: str) -> None:
        self.__method = new_method

    def __str__(self) -> str:
        return f"Payment #{self.__payment_id} - Method: {self.__method}, Amount: {self.__amount}"
