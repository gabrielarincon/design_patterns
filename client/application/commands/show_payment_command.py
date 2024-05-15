from application.commands import Command
from domain.payments.payment import Payment


class ShowPaymentCommand(Command):
    def __init__(self, payment: Payment):
        self.payment = payment

    def execute(self):
        print(f"Payment initiated: {self.payment.generate_payment()}\n")
