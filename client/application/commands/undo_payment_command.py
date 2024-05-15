from json import dumps
from application.commands import Command


class UndoPaymentCommand(Command):
    def __init__(self, publisher, data_store):
        self.data_store = data_store
        self.publisher = publisher

    def execute(self):
        existing_payments = self.data_store.load_payments()
        if existing_payments:
            last_payment = existing_payments.pop()

            last_payment.update({"status": "canceled"})
            print(f"Undoing last payment: {last_payment}")
            self.publisher.publish_message(dumps(last_payment))

            self.data_store.payments = existing_payments
            self.data_store.save_payments()
        else:
            print("No payments to undo.")
