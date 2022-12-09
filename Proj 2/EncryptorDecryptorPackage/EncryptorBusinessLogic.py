import base64
import binascii
import os
import secrets

import pbkdf2
import pyaes


class EncryptorBusinessLogic:
    def __init__(self, key_path):
        self.key = open(key_path, "r").read()
        self.initial_vector = None

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
        return binascii.hexlify(self.key)

    def generate_initial_vector_for_ctr_mode(self, size=16):
        """
        Generate an initial vector for ctr mode encryption
        :return: the initial vector
        """
        self.initial_vector = secrets.token_bytes(size)
        return self.initial_vector

    def __encrypt(self, plaintext):
        """
        Encrypt the given plaintext
        :param plaintext: the plaintext to encrypt
        :return: the ciphertext
        """
        int_initial_vector = int.from_bytes(self.initial_vector, byteorder="big")
        print("Initial vector: " + str(int_initial_vector))
        print("Key: " + str(self.key))
        aes = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(int_initial_vector))
        return aes.encrypt(plaintext)

    def encrypt(self, plaintext_path):
        """
        Encrypt the given plaintext file
        :param plaintext_path: the plaintext file to encrypt
        :return: the ciphertext
        """
        plaintext = open(plaintext_path, "r").read()
        print("Encrypting...")
        print("Plaintext: " + plaintext)
        ciphertext = self.__encrypt(plaintext)
        print("Ciphertext: " + str(ciphertext))
        write_path = os.path.join(os.path.dirname(plaintext_path), "ciphertext")
        self.write_to_file(ciphertext, write_path + ".enc")
        self.write_to_file(str(ciphertext), write_path + ".txt", "w")
        return ciphertext

    @staticmethod
    def write_to_file(data, file_path, mode="wb"):
        """
        Write the given data to the given file path
        :param data: the data to write
        :param file_path: the file path to write to
        :param mode: the mode to write in
        """
        with open(file_path, mode) as file:
            file.write(data)

    def save_data(self, file_path):
        """
        Saves the initial vector and the key to the given file path
        :param file_path: the file path to save to
        """
        self.write_to_file(self.initial_vector, file_path + ".iv")
        self.write_to_file(self.key, file_path + ".key")
        return "Saved data to file"
