import base64
import binascii
import os

import pbkdf2


class EncryptorBusinessLogic:
    def __init__(self, key_path):
        self.key = open(key_path, "r").read()

    @staticmethod
    def generate_salt():
        """
        Generate a salt
        :return: the salt
        """
        salt = os.urandom(16)
        return str(base64.b64encode(salt))[2:-1]

    def add_salt_to_key(self):
        """
        Add a salt to the key
        :return: the new key
        """
        salt = self.generate_salt()
        self.key = self.key + salt
        return self.key

    def change_key_size(self, key_size):
        """
        Change the key size to the given key size

        :param key_size: the key size to change to (in bits)
        :return: the new key
        """
        self.key = pbkdf2.PBKDF2(self.key, self.key).read(key_size // 8)
        return self.key

    def show_hex_key(self):
        """
        Show the key in hexadecimal
        :return: the key in hexadecimal
        """
        return binascii.b2a_hex(self.key)
