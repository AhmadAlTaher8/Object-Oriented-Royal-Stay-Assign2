"""
main.py
This file runs two test cases for the Royal Stay Hotel Management System.
Test cases include: Donald Trump and Joe Biden.
Each test case demonstrates account creation, booking, invoice generation,
payment processing, reservation history display, guest interaction, and cancellation.
"""

from datetime import date
from guest import Guest
from room import Room
from booking import Booking
from invoice import Invoice
from credit_card_payment import CreditCardPayment
from loyalty_program import LoyaltyProgram
from guest_interaction import GuestInteraction

def test_donald_trump():
    print("===== Test Case: Donald Trump =====")
    # Guest Account Creation with Loyalty Program
    loyalty_donald = LoyaltyProgram(points=500, tier="Gold")
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
