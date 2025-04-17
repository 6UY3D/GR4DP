import hashlib
import time

class ProofOfSpaceAndTime:
    def __init__(self, space_allocation_gb=1):
        self.space_allocation_gb = space_allocation_gb

    def generate_proof(self, block_data):
        payload = (str(block_data) + str(time.time()) + str(self.space_allocation_gb)).encode()
        return hashlib.sha256(payload).hexdigest()

    def verify_proof(self, proof, difficulty=3):
        prefix = "0" * difficulty
        return proof.startswith(prefix)
