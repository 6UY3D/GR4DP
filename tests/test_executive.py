import unittest
import time
from gr4dp.exec.executive import Executive
from gr4dp.ledger.ledger import Ledger
from gr4dp.models.self_model import SelfModel
from gr4dp.models.world_model import WorldModel
from gr4dp.models.integrator import Integrator

class TestExecutive(unittest.TestCase):
    def test_executive_run_stop(self):
        ledger = Ledger()
        s_model = SelfModel()
        w_model = WorldModel()
        integrator = Integrator()

        exec_ = Executive(ledger, s_model, w_model, integrator)
        exec_.start()
        time.sleep(2)
        exec_.stop()
        self.assertFalse(exec_.running)
