from typing import List

from application.executors.logger import PaymentLogger
from application.executors.writter import PaymentWriter
from application.file_reader import PaymentFileReader
from domain.payment import Payment
from domain.payment_methods.cash import CashPayment
from domain.payment_methods.credit import CreditPayment
from domain.payment_methods.debit import DebitPayment
from domain.payment_methods.pse import PsePayment
from application.payment_processor import PaymentProcessor


class OnlineProcessor:

    def __init__(self):
        self.processor = PaymentProcessor()
        self.set_cash_payment()
        self.set_credit_payment()
        self.set_debit_payment()
        self.set_pse_payment()

    def process(self, record):
        payment = Payment(**record)
        self.processor.process_payment(payment)

    def set_cash_payment(self):
        cash = CashPayment()
        cash.add_observer(PaymentLogger)
        cash.add_observer(PaymentWriter)
        self.processor.add_payment_method("cash", cash)

    def set_credit_payment(self):
        credit = CreditPayment()
        credit.add_observer(PaymentLogger)
        credit.add_observer(PaymentWriter)
        self.processor.add_payment_method("credit", credit)

    def set_debit_payment(self):
        debit = DebitPayment()
        debit.add_observer(PaymentLogger)
        debit.add_observer(PaymentWriter)
        self.processor.add_payment_method("debit", debit)

    def set_pse_payment(self):
        pse = PsePayment()
        pse.add_observer(PaymentLogger)
        pse.add_observer(PaymentWriter)
        self.processor.add_payment_method("pse", pse)
