import time
import hashlib

class Block:
    def __init__(self, prev_hash, knowledge_commits, proof="", index=0):
        self.prev_hash = prev_hash
        self.index = index
        self.timestamp = int(time.time())
        self.knowledge_commits = knowledge_commits
        self.merkle_root = self._calculate_merkle_root(knowledge_commits)
        self.proof = proof
        self.block_hash = self._calculate_block_hash()

    def _calculate_merkle_root(self, commits):
        combined = "".join([str(c) for c in commits])
        return hashlib.sha256(combined.encode("utf-8")).hexdigest()

    def _calculate_block_hash(self):
        header = f"{self.prev_hash}{self.index}{self.timestamp}{self.merkle_root}{self.proof}"
        return hashlib.sha256(header.encode("utf-8")).hexdigest()

    def __repr__(self):
        return (
            f"Block(index={self.index}, hash={self.block_hash[:10]}..., "
            f"prev={self.prev_hash[:10]}..., proof={self.proof[:6]}..., "
            f"ts={self.timestamp}, commits_count={len(self.knowledge_commits)})"
        )
