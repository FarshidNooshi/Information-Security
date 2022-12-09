import os

import pyfiglet

from EncryptorDecryptorPackage.DecryptorBusinessLogic import DecryptorBusinessLogic
from EncryptorDecryptorPackage.EncryptorBusinessLogic import EncryptorBusinessLogic

DATA_PATH = os.path.join(os.path.dirname(__file__), "EncryptorDecryptorPackage/data")
KEY_FILE_PATH = os.path.join(DATA_PATH, "key.txt")
PROGRAM_DATA_PATH = os.path.join(DATA_PATH, "program", 'data')


def separate_lines_in_terminal():
    print(
        "-" * 100)


def demo():
    print(pyfiglet.figlet_format('Demo'))
    demo_encryptor = EncryptorBusinessLogic(KEY_FILE_PATH)
    key = demo_encryptor.key
    print(f"Key: {key}")
    print(f"Key length: {len(key)}")
    print(f'sample salt: {demo_encryptor.generate_salt()}')
    print(f"Key with salt: {demo_encryptor.add_salt_to_key()}")
    separate_lines_in_terminal()
    print(f"Key with salt length in bytes: {len(demo_encryptor.key)}")
    print(f"Key with salt and key size of 256 bits: {demo_encryptor.change_key_size(256)}")
    print(f"Key with salt and key size of 256 bits length in bytes: {len(demo_encryptor.key)}")
    print(f"Key with salt and key size of 256 bits in hexadecimal: {demo_encryptor.show_hex_key()}")
    print(
        f"Key with salt and key size of 256 bits in hexadecimal length in bytes: {len(demo_encryptor.show_hex_key())}")
    separate_lines_in_terminal()
    print(f"Initial vector for ctr mode: {demo_encryptor.generate_initial_vector_for_ctr_mode()}")
    print(f"Initial vector for ctr mode length in bytes: {len(demo_encryptor.generate_initial_vector_for_ctr_mode())}")
    separate_lines_in_terminal()
    encrypted_text = demo_encryptor.encrypt("EncryptorDecryptorPackage/data/text.txt")
    print(f"Encrypted text: {encrypted_text}")
    print(f"Encrypted text length in bytes: {len(encrypted_text)}")
    separate_lines_in_terminal()
    print(f"saving key to file: {demo_encryptor.save_data(PROGRAM_DATA_PATH)}")
    separate_lines_in_terminal()
    demo_decryptor = DecryptorBusinessLogic(PROGRAM_DATA_PATH)
    decrypted_text = demo_decryptor.decrypt(os.path.join(DATA_PATH, "ciphertext.enc"))
    print(f"Decrypted text: {decrypted_text}")
    print(f"Decrypted text length in bytes: {len(decrypted_text)}")
    separate_lines_in_terminal()
    delete_demo_files()


def delete_demo_files():
    print("Deleting demo files...")
    os.remove(os.path.join(DATA_PATH, "ciphertext.enc"))
    os.remove(os.path.join(DATA_PATH, "ciphertext.txt"))
    os.remove(os.path.join(DATA_PATH, "decrypted.dec"))
    os.remove(os.path.join(PROGRAM_DATA_PATH + ".iv"))
    os.remove(os.path.join(PROGRAM_DATA_PATH + ".key"))
    print("Demo files deleted.")


if __name__ == '__main__':
    demo()
    for i in range(0, 5):
        print("\n")
    print(pyfiglet.figlet_format('Encryptor Decryptor CLI'))
    while True:
        user_input = input("Enter 'e' to encrypt or 'd' to decrypt or 'q' to quit: ")
        if user_input == 'e':
            encryptor = EncryptorBusinessLogic(KEY_FILE_PATH)
            encryptor.add_salt_to_key()
            encryptor.change_key_size(256)
            encryptor.generate_initial_vector_for_ctr_mode()
            encryptor.encrypt(input("Enter the path of the file to encrypt: "))
            encryptor.save_data(PROGRAM_DATA_PATH)
        elif user_input == 'd':
            decryptor = DecryptorBusinessLogic(PROGRAM_DATA_PATH)
            decrypted_text = decryptor.decrypt(input("Enter the path of the file to decrypt: "))
        elif user_input == 'q':
            break
