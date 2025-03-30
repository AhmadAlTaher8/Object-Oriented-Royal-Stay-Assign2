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
