"""
full_Code.py
Royal Stay Hotel Management System - Full Version in a Single File

This file contains the complete implementation of the Royal Stay Hotel Management System,
including all classes and test cases merged into one Python file.

Starting from:
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

"""
guest_interaction.py
Defines the GuestInteraction class for handling both feedback and service requests.
"""

from guest import Guest

class GuestInteraction:
    """
    The GuestInteraction class represents any interaction a guest makes, such as
    submitting feedback or requesting a service.
    """

    def __init__(self, interaction_id: int, guest: Guest, itype: str, message: str, status: str = "Open"):
        """
        Initializes a new GuestInteraction object.

        :param interaction_id: Unique ID for this interaction.
        :param guest: The Guest who initiated the interaction.
        :param itype: The type of interaction (e.g., "Feedback", "ServiceRequest").
        :param message: The content of the feedback or request.
        :param status: Current status of the interaction (Open, InProgress, Closed).
        """
        self.__interaction_id = interaction_id
        self.__guest = guest
        self.__type = itype
        self.__message = message
        self.__status = status

    def submit_interaction(self) -> None:
        """Simulates submitting the interaction."""
        print(f"Interaction #{self.__interaction_id} of type '{self.__type}' submitted by {self.__guest.get_name()}.")

    # Getters and Setters
    def get_interaction_id(self) -> int:
        return self.__interaction_id

    def get_guest(self) -> Guest:
        return self.__guest

    def get_type(self) -> str:
        return self.__type

    def set_type(self, new_type: str) -> None:
        self.__type = new_type

    def get_message(self) -> str:
        return self.__message

    def set_message(self, new_message: str) -> None:
        self.__message = new_message

    def get_status(self) -> str:
        return self.__status

    def set_status(self, new_status: str) -> None:
        self.__status = new_status

    def __str__(self) -> str:
        return (
            f"Interaction #{self.__interaction_id} | "
            f"Type: {self.__type} | "
            f"Status: {self.__status}"
        )

"""
loyalty_program.py
Defines the LoyaltyProgram class for the hotel management system.
"""

class LoyaltyProgram:
    """
    The LoyaltyProgram class tracks loyalty points and tier status for a guest.
    """

    def __init__(self, points: int = 0, tier: str = "Basic"):
        """
        Initializes a new LoyaltyProgram object.

        :param points: The initial loyalty points for the guest.
        :param tier: The loyalty tier (e.g., Basic, Silver, Gold, Platinum).
        """
        self.__points = points
        self.__tier = tier

    def add_points(self, amount: int) -> None:
        """
        Adds loyalty points to the guest's account.
        """
        self.__points += amount
        print(f"Added {amount} points. Total now: {self.__points}")

    def redeem(self, amount: int) -> None:
        """
        Redeems a certain number of points if available.
        """
        if amount <= self.__points:
            self.__points -= amount
            print(f"Redeemed {amount} points. Remaining: {self.__points}")
        else:
            print("Not enough points to redeem.")

    def get_points(self) -> int:
        """Returns the current loyalty points."""
        return self.__points

    def set_points(self, new_points: int) -> None:
        self.__points = new_points

    def get_tier(self) -> str:
        """Returns the current loyalty tier."""
        return self.__tier

    def set_tier(self, new_tier: str) -> None:
        self.__tier = new_tier

    def __str__(self) -> str:
        return f"Loyalty Program: {self.__tier} Tier with {self.__points} points."


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


"""
room.py
Defines the Room class for the hotel management system.
"""

class Room:
    """
    The Room class represents a hotel room with basic attributes and methods.
    """

    def __init__(self, room_number: int, room_type: str, amenities: list, price_per_night: float, is_available: bool = True):
        """
        Initializes a new Room object.

        :param room_number: The unique room number.
        :param room_type: The type of the room (e.g., single, double, suite).
        :param amenities: A list of amenities available in the room.
        :param price_per_night: The cost per night for the room.
        :param is_available: Availability status of the room.
        """
        self.__room_number = room_number
        self.__room_type = room_type
        self.__amenities = amenities
        self.__price_per_night = price_per_night
        self.__is_available = is_available



    # Setters & Getters
    def get_room_number(self) -> int:
        """Returns the room number."""
        return self.__room_number

    def get_room_type(self) -> str:
        """Returns the type of the room."""
        return self.__room_type

    def get_amenities(self) -> list:
        """Returns the list of amenities."""
        return self.__amenities

    def get_price_per_night(self) -> float:
        """Returns the room's nightly price."""
        return self.__price_per_night

    def set_price_per_night(self, new_price: float) -> None:
        """Sets a new price per night for the room."""
        self.__price_per_night = new_price

    def is_available(self) -> bool:
        """Returns True if the room is available, False otherwise."""
        return self.__is_available

    def set_availability(self, status: bool) -> None:
        """
        Updates the availability status of the room.

        :param status: Boolean indicating if the room is available.
        """
        self.__is_available = status

    def get_details(self) -> str:
        """Returns a string with key details about the room."""
        return (
            f"Room {self.__room_number} [{self.__room_type}] "
            f"- Amenities: {', '.join(self.__amenities)} "
            f"- Price/Night: {self.__price_per_night} "
            f"- Available: {self.__is_available}"
        )

    def __str__(self) -> str:
        """Returns a string representation of the Room."""
        return self.get_details()


"""
booking.py
Defines the Booking class for the hotel management system.
"""

from datetime import date
from guest import Guest
from room import Room

class Booking:
    """
    The Booking class manages reservation details for a specific guest and room.
    """

    def __init__(self, booking_id: int, guest: Guest, room: Room,
                 check_in: date, check_out: date, status: str = "Pending"):
        """
        Initializes a new Booking object.

        :param booking_id: Unique ID for the booking.
        :param guest: The Guest object making the booking.
        :param room: The Room object being booked.
        :param check_in: The check-in date.
        :param check_out: The check-out date.
        :param status: Current status of the booking (Pending, Confirmed, Cancelled).
        """
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room    # Composition relationship
        self.__check_in = check_in
        self.__check_out = check_out
        self.__status = status

    def confirm_booking(self) -> None:
        """
        Confirms the booking and marks the room as unavailable.
        """
        self.__status = "Confirmed"
        self.__room.set_availability(False)
        print(f"Booking {self.__booking_id} confirmed for {self.__guest.get_name()}.")

    def cancel_booking(self) -> None:
        """
        Cancels the booking and frees up the room (if it was confirmed).
        """
        self.__status = "Cancelled"
        self.__room.set_availability(True)
        print(f"Booking {self.__booking_id} cancelled.")

    # Getters and Setters
    def get_booking_id(self) -> int:
        return self.__booking_id

    def get_guest(self) -> Guest:
        return self.__guest

    def get_room(self) -> Room:
        return self.__room

    def get_check_in(self) -> date:
        return self.__check_in

    def get_check_out(self) -> date:
        return self.__check_out

    def get_status(self) -> str:
        return self.__status

    def set_status(self, new_status: str) -> None:
        self.__status = new_status

    def __str__(self) -> str:
        return (
            f"Booking #{self.__booking_id} | "
            f"Guest: {self.__guest.get_name()} | "
            f"Room: {self.__room.get_room_number()} | "
            f"Status: {self.__status}"
        )


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


"""
main.py
This file runs two test cases for the Royal Stay Hotel Management System.
Test cases include: Donald Trump and Joe Biden.
Each test case demonstrates account creation, booking, invoice generation,
payment processing, reservation history display, guest interaction, and cancellation.
"""

from datetime import date


def test_donald_trump():
    print("===== Test Case: Donald Trump =====")
    # Guest Account Creation with Loyalty Program
    loyalty_donald = LoyaltyProgram(points=500, tier="Gold")
    # Exception Handling: Try redeeming too many points
    try:
        loyalty_donald.redeem(10000)  # too many points
    except Exception as e:
        print(f"Exception: {e}")
    donald = Guest(name="Donald Trump", email="donald@trump.com", phone="555-0101", loyalty=loyalty_donald)
    donald.create_account()

    # Searching for Available Rooms and Making a Reservation
    room1 = Room(room_number=101, room_type="Suite", amenities=["Wi-Fi", "TV", "Mini-bar"], price_per_night=300.0)
    booking1 = Booking(booking_id=1, guest=donald, room=room1,
                       check_in=date(2025, 4, 1), check_out=date(2025, 4, 5))
    booking1.confirm_booking()

    # Invoice Generation for the Booking
    invoice1 = Invoice(invoice_id=1001, booking=booking1)
    print(invoice1.generate_invoice())

    # Processing Payment using Credit Card
    payment1 = CreditCardPayment(payment_id=5001, amount=invoice1.get_total(), method="Credit Card",
                                 card_number="1234567812345678", expiry_date="12/28")
    if payment1.process_payment():
        print("Payment processed successfully for Donald Trump.")

    # Displaying Reservation History
    donald.view_history()

    # Guest Interaction: Feedback Submission
    interaction1 = GuestInteraction(interaction_id=101, guest=donald,
                                    itype="Feedback", message="Excellent service and luxurious stay!")
    interaction1.submit_interaction()

    # Cancellation of a Reservation: Create and then cancel a new booking
    booking_cancel = Booking(booking_id=2, guest=donald, room=room1,
                             check_in=date(2025, 4, 10), check_out=date(2025, 4, 12))
    booking_cancel.confirm_booking()
    booking_cancel.cancel_booking()
    print("===================================\n")


def test_joe_biden():
    print("===== Test Case: Joe Biden =====")
    # Guest Account Creation with Loyalty Program
    loyalty_joe = LoyaltyProgram(points=300, tier="Silver")
    # Exception Handling: Try redeeming too many points
    try:
        loyalty_joe.redeem(10000)
    except Exception as e:
        print(f"Exception: {e}")
    joe = Guest(name="Joe Biden", email="joe@biden.com", phone="555-0202", loyalty=loyalty_joe)
    joe.create_account()

    # Searching for Available Rooms and Making a Reservation
    room2 = Room(room_number=102, room_type="Double", amenities=["Wi-Fi", "TV"], price_per_night=200.0)
    booking2 = Booking(booking_id=3, guest=joe, room=room2,
                       check_in=date(2025, 5, 1), check_out=date(2025, 5, 3))
    booking2.confirm_booking()

    # Invoice Generation for the Booking
    invoice2 = Invoice(invoice_id=1002, booking=booking2)
    print(invoice2.generate_invoice())

    # Processing Payment using Credit Card
    payment2 = CreditCardPayment(payment_id=5002, amount=invoice2.get_total(), method="Credit Card",
                                 card_number="8765432187654321", expiry_date="11/27")
    if payment2.process_payment():
        print("Payment processed successfully for Joe Biden.")

    # Displaying Reservation History
    joe.view_history()

    # Guest Interaction: Service Request Submission
    interaction2 = GuestInteraction(interaction_id=102, guest=joe,
                                    itype="ServiceRequest", message="Need extra pillows and towels.")
    interaction2.submit_interaction()

    # Cancellation of a Reservation
    booking2.cancel_booking()
    print("===================================\n")


def main():
    test_donald_trump()
    test_joe_biden()


if __name__ == "__main__":
    main()