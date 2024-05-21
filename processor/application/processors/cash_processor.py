from application.executors.logger import PaymentLogger
from application.executors.writter import PaymentWriter
from application.processors import PaymentProcessorTemplate
from domain.payment_methods.cash import CashPayment


class CashProcessor(PaymentProcessorTemplate):

    def set_payment_method(self) -> None:
        self.payment_method = CashPayment()
        self.processor.add_payment_method("cash", self.payment_method)
        print("Cash payment method set.")

    def set_observers(self) -> None:
        self.payment_method.add_observer(PaymentLogger)
        self.payment_method.add_observer(PaymentWriter)
