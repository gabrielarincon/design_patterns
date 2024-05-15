from application.commands import Command


class AddDiscountCommand(Command):
    def __init__(self, payment, reason, discount_type, value):
        self.payment = payment
        self.reason = reason
        self.discount_type = discount_type
        self.value = value

    def execute(self):
        self.payment.add_discount(self.reason, self.discount_type, self.value)
        print(
            f"Discount added to payment {self.payment.reference}: {self.payment.generate_payment()}"
        )
