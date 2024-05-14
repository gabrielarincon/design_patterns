from application.commands import Command
from domain.payments.payment import Payment


class AddPaymentCommand(Command):
    def __init__(self, payment_method, amount):
        self.payment_method = payment_method
        self.amount = amount
        self.payment = None

    def execute(self):
        self.payment = Payment(payment_method=self.payment_method, amount=self.amount)
        print(f"Payment initiated: {self.payment.generate_payment()}")
