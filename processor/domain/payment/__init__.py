from abc import ABC, abstractmethod
from typing import List, Optional


class BasePayment(ABC):
    @abstractmethod
    def apply_charge(self) -> object:
        pass


class Payment(BasePayment):
    def __init__(
        self,
        reference: str,
        payment_method: str,
        amount: float,
        discounts: List = [],
        to_charge: Optional[float] = None,
        status: str = "Pending",
        ):
        self.reference = reference
        self.payment_method = payment_method
        self.amount = amount
        self.discounts = discounts
        self.to_charge = to_charge
        self.status = status

    def apply_charge(self) -> 'Payment':
        if not self.to_charge:
            self.to_charge = self.amount

        return self
