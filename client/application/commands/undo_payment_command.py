from application.commands import Command


class UndoPaymentCommand(Command):
    def __init__(self, publisher, data_store):
        self.data_store = data_store
        self.publisher = publisher

    def execute(self):
        existing_payments = self.data_store.load_payments()
        if existing_payments:
            last_payment = existing_payments.pop()
            self.data_store.payments = existing_payments
            self.data_store.save_payments()
            print(f"Undoing last payment: {last_payment}")
        else:
            print("No payments to undo.")
