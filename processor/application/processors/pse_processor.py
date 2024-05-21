from application.executors.logger import PaymentLogger
from application.executors.writter import PaymentWriter
from application.processors import PaymentProcessorTemplate
from domain.payment_methods.pse import PsePayment


class PseProcessor(PaymentProcessorTemplate):

    def set_payment_method(self) -> None:
        self.payment_method = PsePayment()
        self.processor.add_payment_method("pse", self.payment_method)
        print("Pse payment method set.")

    def set_observers(self) -> None:
        self.payment_method.add_observer(PaymentLogger)
        self.payment_method.add_observer(PaymentWriter)
