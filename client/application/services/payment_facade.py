from application.commands.add_payment_command import AddPaymentCommand
from application.commands.add_discount_command import AddDiscountCommand
from application.commands.pay_command import PayCommand
from application.commands.undo_payment_command import UndoPaymentCommand
from application.commands.show_payment_command import ShowPaymentCommand
from application.data_store import DataStore
from application.publisher import Publisher


class PaymentFacade:
    def __init__(self, data_store: DataStore, publisher: Publisher):
        self.data_store = data_store
        self.publisher = publisher
        self.payment_cmd = None

    def add_payment(self, payment_method, amount):
        self.payment_cmd = AddPaymentCommand(payment_method=payment_method, amount=amount)
        self.payment_cmd.execute()

    def add_discount(self, reason, discount_type, value):
        if self.payment_cmd:
            add_discount_command = AddDiscountCommand(
                payment=self.payment_cmd.payment,
                reason=reason,
                discount_type=discount_type,
                value=value,
            )
            add_discount_command.execute()
        else:
            print("Please add a payment first.")

    def pay(self):
        if self.payment_cmd:
            pay_command = PayCommand(
                payment=self.payment_cmd.payment,
                publisher=self.publisher,
                data_store=self.data_store,
            )
            pay_command.execute()
        else:
            print("Please add a payment first.")

    def undo(self):
        undo_payment_command = UndoPaymentCommand(
            publisher=self.publisher,
            data_store=self.data_store,
        )
        undo_payment_command.execute()

    def show_payment(self):
        if self.payment_cmd:
            show_payment_command = ShowPaymentCommand(payment=self.payment_cmd.payment)
            show_payment_command.execute()
