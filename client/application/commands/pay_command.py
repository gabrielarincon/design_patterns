from json import dumps
from application.commands import Command
import time 


class PayCommand(Command):
    def __init__(self, payment, publisher, data_store):
        self.payment = payment
        self.publisher = publisher
        self.data_store = data_store

    def execute(self):
        payment = self.payment.generate_payment()
        self.data_store.payments.append(payment)
        self.data_store.save_payments()
        print("\nPlease wait...a Morty is processing your payment")
        print(f"processing payment {payment}...")
        time.sleep(3)
        self.publisher.publish_message(dumps(payment))
