from application.commands import Command


class PayCommand(Command):
    def __init__(self, payment, data_store):
        self.payment = payment
        self.data_store = data_store

    def execute(self):
        existing_payments = self.data_store.load_payments()
        existing_payments.append(self.payment.generate_payment())
        self.data_store.payments = existing_payments
        self.data_store.save_payments()
