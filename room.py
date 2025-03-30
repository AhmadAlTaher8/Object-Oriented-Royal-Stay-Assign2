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