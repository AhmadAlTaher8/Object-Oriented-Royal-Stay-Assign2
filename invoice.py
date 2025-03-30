"""
invoice.py
Defines the Invoice class for the hotel management system.
"""

from booking import Booking

class Invoice:
    """
    The Invoice class represents a billing record generated for a booking.
    """

    def __init__(self, invoice_id: int, booking: Booking, total: float = 0.0):
        """
        Initializes a new Invoice object.

        :param invoice_id: Unique ID for the invoice.
        :param booking: The associated Booking object.
        :param total: The total amount billed on this invoice.
        """
        self.__invoice_id = invoice_id
        self.__booking = booking
        self.__total = total

    def generate_invoice(self) -> str:
        """
        Generates a summary of charges based on the booking and returns it as a string.
        """
        # Example logic: total might be based on room price, nights, plus fees
        nights = (self.__booking.get_check_out() - self.__booking.get_check_in()).days
        room_price = self.__booking.get_room().get_price_per_night()
        self.__total = nights * room_price
        return (
            f"Invoice #{self.__invoice_id}\n"
            f"Booking ID: {self.__booking.get_booking_id()}\n"
            f"Guest: {self.__booking.get_guest().get_name()}\n"
            f"Room: {self.__booking.get_room().get_room_number()}\n"
            f"Check-In: {self.__booking.get_check_in()}\n"
            f"Check-Out: {self.__booking.get_check_out()}\n"
            f"Total Due: {self.__total} \n"
        )

    # Getters and Setters
    def get_invoice_id(self) -> int:
        return self.__invoice_id

    def get_booking(self) -> Booking:
        return self.__booking

    def get_total(self) -> float:
        return self.__total

    def set_total(self, amount: float) -> None:
        self.__total = amount

    def __str__(self) -> str:
        return f"Invoice #{self.__invoice_id} for Booking #{self.__booking.get_booking_id()}"
