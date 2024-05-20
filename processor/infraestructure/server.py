import logging
from abc import ABC, abstractmethod
from json import loads

import redis
from application.services.process_payment import PaymentApplication

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class IMessageBroker(ABC):
    @abstractmethod
    def subscribe(self, channel: str):
        pass

    @abstractmethod
    def listen(self, app):
        pass

    @abstractmethod
    def handle_message(self, message, app):
        pass


class RedisAdapter(IMessageBroker):
    def __init__(self):
        self.redis_client = redis.Redis(host="redis", port=6379, db=0)
        self.pubsub = self.redis_client.pubsub()

    def subscribe(self, channel: str):
        """"""
        self.pubsub.subscribe(channel)
        logger.info(f"Subscribed to {channel}")

    def listen(self, app: PaymentApplication):
        for message in self.pubsub.listen():
            if message["type"] == "message":
                self.handle_message(message["data"], app)

    def handle_message(self, message, app):
        payment = message.decode("utf-8")
        logger.info(f"Message received: {payment}")
        app.process(loads(payment))


class Server:
    def __init__(self, app: PaymentApplication):
        self.broker = RedisAdapter()
        self.app = app

    def run(self):
        self.broker.subscribe(channel="payment_message")
        self.broker.listen(self.app)
