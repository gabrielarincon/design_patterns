import logging
from abc import ABC, abstractmethod

import redis

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("client")


class AbstractPublisher(ABC):
    def __init__(self, redis_host="redis", redis_port=6379):
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_client = redis.Redis(host=self.redis_host, port=self.redis_port, db=0)

    @abstractmethod
    def publish_message(self, message):
        pass


class Publisher(AbstractPublisher):
    def __init__(self, redis_host="redis", redis_port=6379, channel="payment_message"):
        super().__init__(redis_host, redis_port)
        self.channel = channel

    def publish_message(self, message):
        self.redis_client.publish(self.channel, message)
        logger.info(f"payment published: {message}")
