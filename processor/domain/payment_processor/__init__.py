from abc import ABC, abstractmethod

from domain.discounts import DiscountPaymentFactory

from domain.payment import Payment
from domain.payment_methods import PaymentMethod


class AbstractPaymentProcessor(ABC):
    @abstractmethod
    def add_payment_method(self, payment_method, strategy):
        pass

    @abstractmethod
    def remove_payment_method(self, payment_method):
        pass

    @abstractmethod
    def process_payment(self, payment):
        pass


class PaymentProcessor(AbstractPaymentProcessor):
    def __init__(self):
        self.payment_strategies = {}

    def add_payment_method(self, payment_method: str, strategy: PaymentMethod):
        """Add a payment method to the processor"""
        self.payment_strategies[payment_method] = strategy

    def remove_payment_method(self, payment_method: str):
        """Remove a payment method from the processor"""
        if payment_method in self.payment_strategies:
            del self.payment_strategies[payment_method]

    def process_payment(self, payment: Payment):
        """Process a payment using the specified payment method"""

        payment_method = payment.payment_method
        discount_factory = DiscountPaymentFactory()

        for discount in payment.discounts:
            payment = discount_factory.create_discount(payment, discount)

        if payment_method in self.payment_strategies:
            strategy = self.payment_strategies[payment_method]
            strategy.process_payment(payment)

        else:
            print(f"Error: Payment method '{payment_method}' not found.")
