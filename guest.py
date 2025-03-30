"""
guest.py
Defines the Guest class for the hotel management system.
"""

from loyalty_program import LoyaltyProgram

class Guest:
    """
    The Guest class represents a hotel guest, storing personal info and
    linking to a loyalty program.
    """

    def __init__(self, name: str, email: str, phone: str, loyalty: LoyaltyProgram = None):
        """
        Initializes a new Guest object.

        :param name: The guest's name.
        :param email: The guest's email address.
        :param phone: The guest's phone number.
        :param loyalty: An optional LoyaltyProgram instance.
        """
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__loyalty = loyalty  # Aggregation relationship

    def create_account(self) -> None:
        """Simulates account creation for the guest."""
        print(f"Account created for {self.__name} ({self.__email}).")

    def view_history(self) -> None:
        """Displays the guest's booking history (stub)."""
        print(f"Displaying booking history for {self.__name}.")

    # Getters and Setters
    def get_name(self) -> str:
        """Returns the guest's name."""
        return self.__name

    def set_name(self, name: str) -> None:
        """Sets the guest's name."""
        self.__name = name

    def get_email(self) -> str:
        """Returns the guest's email."""
        return self.__email

    def set_email(self, email: str) -> None:
        """Sets the guest's email."""
        self.__email = email

    def get_phone(self) -> str:
        """Returns the guest's phone number."""
        return self.__phone

    def set_phone(self, phone: str) -> None:
        """Sets the guest's phone number."""
        self.__phone = phone

    def get_loyalty_program(self) -> LoyaltyProgram:
        """Returns the LoyaltyProgram instance associated with the guest."""
        return self.__loyalty

    def set_loyalty_program(self, loyalty: LoyaltyProgram) -> None:
        """Sets the LoyaltyProgram for the guest."""
        self.__loyalty = loyalty

    def __str__(self) -> str:
        """Returns a string representation of the Guest."""
        loyalty_status = "No Loyalty Program" if not self.__loyalty else "Loyalty Program Attached"
        return f"Guest: {self.__name}, Email: {self.__email}, {loyalty_status}"
