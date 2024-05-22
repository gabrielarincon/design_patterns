from abc import ABC, abstractmethod

from domain.payment import Payment
from domain.payment_methods import PaymentMethod
from domain.payment_processor import PaymentProcessor


class PaymentProcessorTemplate(ABC):

    def __init__(self):

        self.payment: Payment
        self.payment_method: PaymentMethod
        self.processor = PaymentProcessor()

    def process_payment(self, record):
        """The template method defines the skeleton of the payment processing algorithm"""
        self.set_payment_method()
        self.set_observers()
        self.initialize_payment(record)
        self.execute_payment()

    @abstractmethod
    def set_payment_method(self):
        """need implementation on abstract class"""

    @abstractmethod
    def set_observers(self):
        """need implementation on abstract class"""

    def initialize_payment(self, record):
        """initize the payment object"""
        self.payment = Payment(**record)
        print(f"Initialized payment with record: {record}")

    def execute_payment(self):
        """executes the payment"""
        self.processor.process_payment(self.payment)
        print("Executed cash payment.")
