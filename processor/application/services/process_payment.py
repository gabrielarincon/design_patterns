from collections.abc import Mapping

from application.processors.cash_processor import CashProcessor
from application.processors.credit_processor import (
    MastercardCreditProcessor,
)
from application.processors.debit_processor import (
    MastercardDebitProcessor,
    VisaDebitProcessor,
)
from application.processors.pse_processor import PseProcessor
from domain.payment import Payment


class PaymentApplication:

    def __init__(self):
        self.processor = {}

    def process_transaction(self, record: Mapping) -> None:
        """process payment transaction"""
        payment = Payment(**record)
        processor_strategy = self.processor.get(payment.payment_method)

        if processor_strategy:
            processor = processor_strategy()
            processor.process_payment(record)
            return

        print(f"Unsupported payment method: {payment.payment_method}")


class UPay(PaymentApplication):

    def __init__(self):
        super().__init__()
        self.processor = {
            "cash": CashProcessor,
            "mastercard-credit": MastercardCreditProcessor,
            "mastercard-debit": MastercardDebitProcessor,
            "visa-debit": VisaDebitProcessor,
            "pse": PseProcessor,
        }


class SoftBank(PaymentApplication):

    def __init__(self):
        super().__init__()
        self.processor = {
            "mastercard-credit": MastercardCreditProcessor,
            "mastercard-debit": MastercardDebitProcessor,
        }


class NuBank(PaymentApplication):

    def __init__(self):
        super().__init__()
        self.processor = {
            "visa-debit": VisaDebitProcessor,
            "visa-credit": MastercardCreditProcessor,
        }
