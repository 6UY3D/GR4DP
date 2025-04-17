import torch

class Integrator:
    def integrate(self, s_embedding, w_embedding):
        return s_embedding + w_embedding

    def update_ledger_memory(self, ledger, s_emb, w_emb, c):
        # Construct a structured knowledge commit
        knowledge_commit = {
            "commit_id": f"commit_c_{hash(c)}",
            "type": "logical",
            "priority": 2,
            "data": {
                "S_embedding": s_emb.cpu().tolist(),
                "W_embedding": w_emb.cpu().tolist(),
                "C_representation": c.cpu().tolist()
            },
            "parents": []
        }
        ledger.add_block([knowledge_commit])
