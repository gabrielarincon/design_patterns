from collections.abc import Mapping
import json
from application.executors import ExecutorObserver


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DataStore(metaclass=SingletonMeta):
    def __init__(self, file_name):
        self.file_name = file_name
        self.payments = self.load_payments()

    def load_payments(self):
        try:
            with open(self.file_name, "r") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return []

    def save_payments(self):
        with open(self.file_name, "w") as json_file:
            json.dump(self.payments, json_file, indent=4)
            print(f"Payments details saved to {self.file_name}")


class PaymentWriter(ExecutorObserver):
    def update(self, payment):
        """Register payment info"""
        data_store = DataStore("payment_details.json")

        existing_record = False
        for idx, _payment in enumerate(data_store.payments):
            if payment.reference == _payment["reference"]:
                data_store.payments[idx] = {**payment.__dict__, "to_charge": 0}
                existing_record = True

        if not existing_record:
            data_store.payments.append({**payment.__dict__, "status": "chargued"})

        data_store.save_payments()


