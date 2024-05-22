from collections.abc import Mapping
from domain.payment import Payment


class PercentageDiscount(Payment):
    def __init__(self, payment: Payment, discount: int):
        self.payment = payment
        self.discount = discount

    def apply_charge(self) -> Payment:
        self.payment = self.payment.apply_charge()
        percentage = self.discount / 100

        if self.payment.to_charge:
            self.payment.to_charge -= self.payment.to_charge * percentage
        else:
            discount_amount = self.payment.amount * percentage
            self.payment.to_charge = self.payment.amount - discount_amount

        return self.payment


class TotalAmountDiscount(Payment):
    def __init__(self, payment: Payment, discount: int):
        self.payment = payment
        self.discount = discount

    def apply_charge(self) -> Payment:
        self.payment = self.payment.apply_charge()

        if self.payment.to_charge:
            self.payment.to_charge -= abs(self.discount)
        else:
            self.payment.to_charge = self.payment.amount - abs(self.discount)
        return self.payment


class DiscountPaymentFactory:
    def create_discount(self, payment: Payment, discount: Mapping) -> Payment:
        if discount.get("discount_type") == "total_amount":
            payment = TotalAmountDiscount(payment, discount["value"])
        elif discount.get("discount_type") == "percentage":
            payment = PercentageDiscount(payment, discount["value"])

        return payment
