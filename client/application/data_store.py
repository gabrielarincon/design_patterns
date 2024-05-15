"""Temporal DataStore Module"""
import json


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
