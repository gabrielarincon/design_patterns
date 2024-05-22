from application.executors.logger import PaymentLogger
from application.executors.writter import PaymentWriter
from application.processors import PaymentProcessorTemplate

from domain.payment_methods.debit import DebitPayment


class DebitProcessor(PaymentProcessorTemplate):

    def set_payment_method(self) -> None:
        self.payment_method = DebitPayment()
        self.processor.add_payment_method("debit", self.payment_method)
        print("Debit payment method set.")

    def set_observers(self) -> None:
        self.payment_method.add_observer(PaymentLogger)
        self.payment_method.add_observer(PaymentWriter)


class VisaDebitProcessor(DebitProcessor):
    """Visa Association Debit Payment Processor"""

    def set_payment_method(self) -> None:
        self.payment_method = DebitPayment()
        self.processor.add_payment_method("visa-debit", self.payment_method)
        print("Visa Debit payment method set.")


class MastercardDebitProcessor(DebitProcessor):
    """MasterCard Association Debit Payment Processor"""

    def set_payment_method(self) -> None:
        self.payment_method = DebitPayment()
        self.processor.add_payment_method("mastercard-debit", self.payment_method)
        print("MasterCard Debit payment method set.")
