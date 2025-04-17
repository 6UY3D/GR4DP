import logging
from gr4dp.ledger.block import Block
from gr4dp.network.consensus import ProofOfSpaceAndTime
from gr4dp.logic.knowledge_manager import KnowledgeManager

class Ledger:
    def __init__(self):
        self.chain = []
        self.consensus = ProofOfSpaceAndTime(space_allocation_gb=1)
        self.logger = logging.getLogger("ledger")
        self.knowledge_manager = KnowledgeManager()

        if not self.chain:
            genesis_block = Block(
                prev_hash="0"*64,
                knowledge_commits=["GENESIS BLOCK"],
                index=0
            )
            self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, knowledge_commits):
        """
        knowledge_commits can be a list of either strings or dictionaries.
        If a dictionary is used, it can contain metadata for hierarchical organization:
          {
            "commit_id": "unique_id_123",
            "type": "empirical" or "logical",
            "priority": int,
            "data": {...custom data...},
            "parents": ["another_commit_id", ...]
          }
        """
        prev_block = self.get_latest_block()
        index = prev_block.index + 1
        candidate = Block(
            prev_hash=prev_block.block_hash,
            knowledge_commits=knowledge_commits,
            index=index
        )

        # Organize each knowledge commit in the manager's hierarchy
        for commit in knowledge_commits:
            # If it's a dictionary, it might have hierarchical metadata
            if isinstance(commit, dict):
                self.knowledge_manager.organize_commit(commit)
            else:
                # If it's just a string or something, wrap it
                wrapped = {
                    "commit_id": f"commit_{index}_{hash(commit)}",
                    "type": "empirical",
                    "priority": 1,
                    "data": commit,
                    "parents": []
                }
                self.knowledge_manager.organize_commit(wrapped)

        # Now do proof-of-space-and-time
        proof = self.consensus.generate_proof(candidate.block_hash)
        if self.consensus.verify_proof(proof, difficulty=3):
            candidate.proof = proof
            candidate.block_hash = candidate._calculate_block_hash()
            self.chain.append(candidate)
            self.logger.info(f"Block {candidate.index} added: {candidate}")
            return candidate
        else:
            self.logger.warning("Invalid proof, block not added.")
            return None
