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
