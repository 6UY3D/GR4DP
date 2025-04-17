import torch
import random
from gr4dp.config import node_context

class ChatManager:
    def process_user_message(self, message: str) -> str:
        """
        Minimal chat function that transforms a user message into an internal representation,
        passes it through S/W, and merges to produce a response.
        Then adds a structured knowledge commit with hierarchy data to the ledger.
        """

        ledger = node_context.get("ledger")
        s_model = node_context.get("self_model")
        w_model = node_context.get("world_model")
        integrator = node_context.get("integrator")

        if not all([ledger, s_model, w_model, integrator]):
            return "Node is not fully initialized; please run the node first."

        # Convert user message into a pseudo embedding
        user_tensor = torch.randn((1, 256))

        s_emb = s_model.reflect(user_tensor)
        w_emb = w_model.reason_about_world(user_tensor)
        c = integrator.integrate(s_emb, w_emb)

        # Generate a minimal textual response
        num = c[0, 0].item()
        system_reply = f"System synergy => {num:.3f}"

        # Create a hierarchical knowledge commit that references the chat
        # For example, we treat the user message as "empirical" input, 
        # and the system reply as "logical" or vice versa
        user_commit = {
            "commit_id": f"user_{hash(message)}",
            "type": "empirical",
            "priority": 1,
            "data": {"message": message},
            "parents": []
        }
        system_commit = {
            "commit_id": f"system_{hash(system_reply)}",
            "type": "logical",
            "priority": 2,
            "data": {"reply": system_reply},
            "parents": [user_commit["commit_id"]]
        }
        # Add them to the ledger in a single block
        ledger.add_block([user_commit, system_commit])

        return system_reply
