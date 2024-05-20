from processor.application.services.process_payment import UPay as App
from processor.infraestructure.server import Server


if __name__ == "__main__":

    app = App()
    server = Server(app)
    server.run()
