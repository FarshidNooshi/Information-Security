import os

import pyaes


class DecryptorBusinessLogic:
    def __init__(self, program_data_path):
        self.program_data_path = program_data_path
        self.key = open(program_data_path + ".key", "rb").read()
        self.initial_vector = open(program_data_path + ".iv", "rb").read()

    def __decrypt(self, ciphertext):
        """
        Decrypt the given ciphertext
        :param ciphertext: the ciphertext to decrypt
        :return: the plaintext
        """
        int_initial_vector = int.from_bytes(self.initial_vector, byteorder="big")
        print("Initial vector: " + str(int_initial_vector))
        print("Key: " + str(self.key))
        aes = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(int_initial_vector))
        return aes.decrypt(ciphertext)

    def decrypt(self, ciphertext_path):
        """
        Decrypt the given ciphertext file
        :param ciphertext_path: the ciphertext file to decrypt
        :return: the plaintext
        """
        ciphertext = open(ciphertext_path, "rb").read()
        print("Decrypting...")
        print("Ciphertext: " + str(ciphertext))
        plaintext = self.__decrypt(ciphertext)
        print("Plaintext: " + str(plaintext))
        write_path = os.path.join(os.path.dirname(ciphertext_path), "decrypted")
        self.write_to_file(plaintext, write_path + ".dec")
        # self.write_to_file(plaintext, write_path + ".txt", "wb")
        return plaintext

    @staticmethod
    def write_to_file(data, file_path, mode="wb"):
        """
        Write the given data to the given file path
        :param data: the data to write in bytes
        :param file_path: the file path to write to
        :param mode: the mode to write in
        """
        with open(file_path, mode) as file:
            file.write(data)
