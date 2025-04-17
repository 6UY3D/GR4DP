import sqlite3
import os

class BlockStore:
    def __init__(self, db_path="data/ledger.db"):
        os.makedirs("data", exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS blocks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                index_num INTEGER,
                prev_hash TEXT,
                block_hash TEXT,
                timestamp INTEGER,
                merkle_root TEXT,
                proof TEXT,
                knowledge_commits TEXT
            )
        """)
        self.conn.commit()

    def save_block(self, block):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO blocks (
                index_num, prev_hash, block_hash, timestamp, merkle_root, proof, knowledge_commits
            ) VALUES (?,?,?,?,?,?,?)
        """, (
            block.index,
            block.prev_hash,
            block.block_hash,
            block.timestamp,
            block.merkle_root,
            block.proof,
            str(block.knowledge_commits)
        ))
        self.conn.commit()
