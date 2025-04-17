import os
import random
from gr4dp.network.p2p_node import P2PNode
from gr4dp.exec.executive import Executive
from gr4dp.ledger.ledger import Ledger
from gr4dp.models.self_model import SelfModel
from gr4dp.models.world_model import WorldModel
from gr4dp.models.integrator import Integrator
from gr4dp.utils.logging_config import setup_logging

# A global dictionary for minimal "shared" references
node_context = {
    "ledger": None,
    "self_model": None,
    "world_model": None,
    "integrator": None,
    "executive": None,
    "p2p_node": None,
}

def initialize_node():
    print("Initializing node environment...")
    os.makedirs("data", exist_ok=True)
    random.seed()

def run_node():
    setup_logging("INFO")

    ledger = Ledger()
    s_model = SelfModel()
    w_model = WorldModel()
    integrator = Integrator()
    p2p_node = P2PNode(ledger=ledger)
    p2p_node.start()

    executive = Executive(
        ledger=ledger,
        self_model=s_model,
        world_model=w_model,
        integrator=integrator
    )
    executive.start()

    node_context["ledger"] = ledger
    node_context["self_model"] = s_model
    node_context["world_model"] = w_model
    node_context["integrator"] = integrator
    node_context["executive"] = executive
    node_context["p2p_node"] = p2p_node

    try:
        import time
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        executive.stop()
        p2p_node.stop()
