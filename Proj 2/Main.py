import os
from EncryptorDecryptorPackage.EncryptorBusinessLogic import EncryptorBusinessLogic

KEY_FILE_PATH = os.path.join(os.path.dirname(__file__), "EncryptorDecryptorPackage/data/key.txt")

if __name__ == '__main__':
    encryptor = EncryptorBusinessLogic(KEY_FILE_PATH)
    key = encryptor.key
    print(f"Key: {key}")
    print(f"Key length: {len(key)}")
    print(f'sample salt: {encryptor.generate_salt()}')
    print(f"Key with salt: {encryptor.add_salt_to_key()}")
