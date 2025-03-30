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
