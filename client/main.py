from application.commands.add_payment_command import AddPaymentCommand
from application.commands.add_discount_command import AddDiscountCommand
from application.commands.pay_command import PayCommand
from application.commands.undo_payment_command import UndoPaymentCommand
from application.commands.show_payment_command import ShowPaymentCommand
from application.data_store import DataStore
from application.publisher import Publisher


class Application:
    def __init__(self):
        self.data_store = DataStore(file_name="payment_details.json")
        self.publisher = Publisher()
        self.payment_cmd = None

    def display_menu(self):
        print(
            """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠙⢿⣦⡀⠀⠀⠀⢀⣾⡿⠉⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠙⣿⣄⣠⣴⡿⠋⠀⠀⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠈⠿⠟⠉⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⣿⡿⠿⠿⠿⠷⣶⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣤⣤⣴⣶⣶⡀
⠀⠀⠀⠹⣿⡀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠚⠉⠉⠉⠉⠛⠲⣄⠀⠈⠉⠉⠉⠁⣼⡟⠀
⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⢀⡔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⢀⣼⡟⠀⠀
⠀⠀⠀⠀⠀⢹⣷⠀⠀⢀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⢠⣾⡏⠀⠀⠀
⠀⢀⣠⣴⡾⠟⠋⠀⠀⣸⠀⠀⠀⣴⣒⣒⣛⣛⣛⣋⣉⣉⣉⣙⣛⣷⠀⠙⠿⣶⣤⡀
⣾⣿⡋⠁⠀⠀⠀⠀⠀⡏⠀⠀⡄⠉⠉⠁⠀⠈⢹⢨⠃⠀⠀⠀⠀⠙⡄⠀⠀⣨⣿⠟
⠈⠛⠿⣷⣦⣀⠀⠀⠀⡇⠀⠸⡟⠛⠿⠛⠛⠛⢻⢿⠋⠹⠟⠉⠉⠙⡇⣠⣾⠟⠁⠀
⠀⠀⠀⢀⣽⣿⠇⠀⠀⡇⠀⠀⠳⣄⣀⠀⣀⣠⠞⠈⢷⣄⣀⣀⣠⣾⠁⢿⣧⡀⠀⠀
⠀⢠⣴⡿⠋⠁⠀⠀⢀⡧⠄⠀⠦⣀⣈⣉⠁⠀⠠⡀⠘⡆⠠⠤⠴⢿⣄⠀⠙⣿⣦⠀
⠀⠹⢿⣦⣤⣀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣤⠇⠀⠀⠀⣼⢘⣷⡿⠟⠋⠀
⠀⠀⠀⠈⠉⣿⡇⠈⠣⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠻⣿⡀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣤⣤⣤⣤⢧⠀⢀⡆⣠⠴⠒⠋⢹⠋⠉⢹⠗⠒⠄⣷⣾⡿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠉⣿⣇⣈⣆⠀⠳⠤⠀⠀⠀⠈⣇⡖⡍⠀⠠⣾⣿⡿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⢻⣷⣄⠀⠀⠀⠀⠁⠉⠀⠀⣠⣾⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣉⣿⣷⠲⠤⠤⠤⣤⣶⣿⣟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣶⡿⠿⠛⠛⢋⢹⡦⣄⣀⡤⢿⢉⠛⠛⠿⣷⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠏⠀⠀⠀⠀⢀⠇⠈⡇⠀⠀⠀⠘⡎⣆⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠿⣶⣶⣶⣶⣶⣾⣶⣾⣷⣶⣶⣶⣶⣷⣾⣷⣶⣶⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

        -- Rick and Morty Payment System --
"Break the cycle, Morty. Rise above. Focus on science."

        1. Add Payment
        2. Add Discount
        3. Pay
        4. Undo
        0. Exit

        Wubba Lubba Dub Dub! Choose an option:
        """
        )

    def run(self):
        while True:
            self.display_menu()
            self.show_payment()

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_payment()
            elif choice == "2":
                self.add_discount()
            elif choice == "3":
                self.pay()
            elif choice == "4":
                self.undo()
            elif choice == "0":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_payment(self):
        payment_method = input("Enter payment method [cash, debit, credit, pse]: ")
        amount = float(input("Enter payment amount: "))
        self.payment_cmd = AddPaymentCommand(payment_method=payment_method, amount=amount)
        self.payment_cmd.execute()

    def add_discount(self):
        if self.payment_cmd:
            reason = input("Enter discount reason: ")
            discount_type = input("Enter discount type [total_amount, percentage]: ")
            value = float(input("Enter discount value: "))
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


if __name__ == "__main__":
    app = Application()
    app.run()
