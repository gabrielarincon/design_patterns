"""Discounts Module"""


class Discounts:
    """Creates a list of discounts that can be applied to a purchase"""

    def __init__(self):
        self.discount_list = []

    def add_discount(self, reason, discount_type, value):
        """Adds a discount to the list of discounts."""
        discount = {
            "reason": reason,
            "discount_type": discount_type,
            "value": value,
        }
        self.discount_list.append(discount)

    def generate_discounts_list(self):
        """Returns the list of discounts."""
        return self.discount_list
