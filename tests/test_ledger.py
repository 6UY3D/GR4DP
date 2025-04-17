import unittest
from gr4dp.ledger.ledger import Ledger

class TestLedger(unittest.TestCase):
    def test_genesis_block(self):
        ledger = Ledger()
        self.assertEqual(len(ledger.chain), 1)

    def test_add_block(self):
        ledger = Ledger()
        block = ledger.add_block(["Test knowledge"])
        self.assertIsNotNone(block)
        self.assertEqual(block.index, 1)
