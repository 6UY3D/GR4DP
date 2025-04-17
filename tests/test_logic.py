import unittest
from gr4dp.logic.theorem_prover import TheoremProver
from gr4dp.logic.modal_logic import ModalLogicEngine
from gr4dp.logic.reasoner import Reasoner
from gr4dp.logic.knowledge_manager import KnowledgeManager

class TestLogic(unittest.TestCase):
    def test_reasoner(self):
        tp = TheoremProver()
        me = ModalLogicEngine()
        r = Reasoner(tp, me)
        proven, proof_steps, modal_eval = r.analyze("Example statement")
        self.assertTrue(proven)
        self.assertTrue(modal_eval)
        self.assertIn("SAMPLE_PROOF_STEP_1", proof_steps)

    def test_knowledge_manager(self):
        km = KnowledgeManager()
        km.organize_commit({
            "commit_id": "c1",
            "type": "empirical",
            "priority": 1,
            "data": {"info": "test"},
            "parents": []
        })
        km.organize_commit({
            "commit_id": "c2",
            "type": "logical",
            "priority": 2,
            "data": {"info": "child"},
            "parents": ["c1"]
        })
        self.assertIn("c1", km.commits_by_id)
        self.assertIn("c2", km.commits_by_id)
        self.assertEqual(km.commits_by_id["c1"].children[0], km.commits_by_id["c2"])
