from application.executors.logger import PaymentLogger
from application.executors.writter import PaymentWriter
from application.processors import PaymentProcessorTemplate
from domain.payment_methods.credit import CreditPayment


class CreditProcessor(PaymentProcessorTemplate):

    def set_payment_method(self) -> None:
        self.payment_method = CreditPayment()
        self.processor.add_payment_method("credit", self.payment_method)
        print("Credit payment method set.")

    def set_observers(self) -> None:
        self.payment_method.add_observer(PaymentLogger)
        self.payment_method.add_observer(PaymentWriter)


class VisaCreditProcessor(CreditProcessor):
    """Visa Association Credit Payment Processor"""

    def set_payment_method(self) -> None:
        self.payment_method = CreditPayment()
        self.processor.add_payment_method("visa-credit", self.payment_method)
        print("Credit payment method set.")


class MastercardCreditProcessor(CreditProcessor):
    """MasterCard Association Credit Payment Processor"""

    def set_payment_method(self) -> None:
        self.payment_method = CreditPayment()
        self.processor.add_payment_method("mastercard-credit", self.payment_method)
        print("MasterCard Credit payment method set.")
