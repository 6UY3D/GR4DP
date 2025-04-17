import os
import hashlib

def generate_random_key():
    return os.urandom(32)

def sha256_hash(data: bytes):
    return hashlib.sha256(data).hexdigest()
