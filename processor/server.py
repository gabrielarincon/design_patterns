import logging
from json import loads
import redis
from main import OnlineProcessor

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class Subscriber:
    def __init__(self, redis_host="redis", redis_port=6379, channel="payment_message"):
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_client = redis.Redis(host=self.redis_host, port=self.redis_port, db=0)
        self.pubsub = self.redis_client.pubsub()
        self.channel = channel

    def subscribe(self):
        self.pubsub.subscribe(self.channel)
        logger.info(f"Subscribed to {self.channel}")

    def listen(self, processor):
        logger.info(f"Listening for messages on {self.channel}")
        for message in self.pubsub.listen():
            if message["type"] == "message":
                self.handle_message(message["data"], processor)

    def handle_message(self, message, processor):
        payment = message.decode("utf-8")
        logger.info(f"Message received: {payment}")
        processor.process(loads(payment))


class Server:
    def __init__(self, subscriber):
        self.subscriber = subscriber
        self.processor = OnlineProcessor()

    def run(self):
        self.subscriber.subscribe()
        self.subscriber.listen(self.processor)


if __name__ == "__main__":
    subscriber = Subscriber()
    server = Server(subscriber)
    server.run()
