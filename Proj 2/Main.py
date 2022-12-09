import os

from EncryptorDecryptorPackage.EncryptorBusinessLogic import EncryptorBusinessLogic
from EncryptorDecryptorPackage.DecryptorBusinessLogic import DecryptorBusinessLogic

DATA_PATH = os.path.join(os.path.dirname(__file__), "EncryptorDecryptorPackage/data")
KEY_FILE_PATH = os.path.join(DATA_PATH, "key.txt")
PROGRAM_DATA_PATH = os.path.join(DATA_PATH, "program", 'data')


def separate_lines_in_terminal():
    print(
        "------------------------------------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    encryptor = EncryptorBusinessLogic(KEY_FILE_PATH)
    key = encryptor.key
    print(f"Key: {key}")
    print(f"Key length: {len(key)}")
    print(f'sample salt: {encryptor.generate_salt()}')
    print(f"Key with salt: {encryptor.add_salt_to_key()}")
    separate_lines_in_terminal()
    print(f"Key with salt length in bytes: {len(encryptor.key)}")
    print(f"Key with salt and key size of 256 bits: {encryptor.change_key_size(256)}")
    print(f"Key with salt and key size of 256 bits length in bytes: {len(encryptor.key)}")
    print(f"Key with salt and key size of 256 bits in hexadecimal: {encryptor.show_hex_key()}")
    print(f"Key with salt and key size of 256 bits in hexadecimal length in bytes: {len(encryptor.show_hex_key())}")
    separate_lines_in_terminal()
    print(f"Initial vector for ctr mode: {encryptor.generate_initial_vector_for_ctr_mode()}")
    print(f"Initial vector for ctr mode length in bytes: {len(encryptor.generate_initial_vector_for_ctr_mode())}")
    separate_lines_in_terminal()
    encrypted_text = encryptor.encrypt("EncryptorDecryptorPackage/data/text.txt")
    print(f"Encrypted text: {encrypted_text}")
    print(f"Encrypted text length in bytes: {len(encrypted_text)}")
    separate_lines_in_terminal()
    print(f"saving key to file: {encryptor.save_data('EncryptorDecryptorPackage/data/program/data')}")
    separate_lines_in_terminal()
    decryptor = DecryptorBusinessLogic(PROGRAM_DATA_PATH)
    decrypted_text = decryptor.decrypt(os.path.join(DATA_PATH, "ciphertext.enc"))
    print(f"Decrypted text: {decrypted_text}")
    print(f"Decrypted text length in bytes: {len(decrypted_text)}")
    separate_lines_in_terminal()
