"""
credit_card_payment.py
Defines the CreditCardPayment class for the hotel management system.
"""

from payment import Payment

class CreditCardPayment(Payment):
    """
    The CreditCardPayment class extends the Payment base class
    to implement credit card-specific attributes and logic.
    """

    def __init__(self, payment_id: int, amount: float, method: str, card_number: str, expiry_date: str):
        """
        Initializes a new CreditCardPayment object.

        :param payment_id: Unique ID for the payment.
        :param amount: The total amount to be paid.
        :param method: The payment method (e.g., "Credit Card").
        :param card_number: The credit card number.
        :param expiry_date: The expiry date of the credit card.
        """
        super().__init__(payment_id, amount, method)
        self.__card_number = card_number
        self.__expiry_date = expiry_date

    def process_payment(self) -> bool:
        """
        Processes the credit card payment. 
        For now, we simulate a successful payment.
        """
        print(f"Processing credit card payment with card number ending in {self.__card_number[-4:]}")
        # Here you would integrate with a payment gateway.
        return True

    # Getters and Setters
    def get_card_number(self) -> str:
        return self.__card_number

    def set_card_number(self, new_card_number: str) -> None:
        self.__card_number = new_card_number

    def get_expiry_date(self) -> str:
        return self.__expiry_date

    def set_expiry_date(self, new_expiry: str) -> None:
        self.__expiry_date = new_expiry

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str} | CC: **** **** **** {self.__card_number[-4:]}"
