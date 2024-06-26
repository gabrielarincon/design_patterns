import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

from application.executors import ExecutorObserver


class PaymentLogger(ExecutorObserver):
    def update(self, payment):
        """Register payment info"""
        logger.info(f"payment processed: {payment.__dict__}")
