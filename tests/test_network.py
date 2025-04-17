import unittest
from gr4dp.network.p2p_node import P2PNode
from gr4dp.ledger.ledger import Ledger

class TestNetwork(unittest.TestCase):
    def test_p2p_node_start_stop(self):
        ledger = Ledger()
        node = P2PNode(ledger=ledger, port=4050)
        node.start()
        self.assertTrue(node.running)
        node.stop()
        self.assertFalse(node.running)
