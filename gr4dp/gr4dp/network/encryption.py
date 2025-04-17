from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self, key=None):
        if key is None:
            key = Fernet.generate_key()
        self.fernet = Fernet(key)

    def encrypt(self, data: bytes) -> bytes:
        return self.fernet.encrypt(data)

    def decrypt(self, token: bytes) -> bytes:
        return self.fernet.decrypt(token)
