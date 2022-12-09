import base64
import os


class EncryptorBusinessLogic:
    def __init__(self, key_path):
        self.key = open(key_path, "r").read()

    @staticmethod
    def generate_salt():
        salt = os.urandom(16)
        return str(base64.b64encode(salt))

    def add_salt_to_key(self):
        salt = self.generate_salt()
        self.key = self.key + salt
        return self.key
