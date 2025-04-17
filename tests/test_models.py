import unittest
import torch
from gr4dp.models.self_model import SelfModel
from gr4dp.models.world_model import WorldModel
from gr4dp.models.integrator import Integrator

class TestModels(unittest.TestCase):
    def test_self_world_integration(self):
        s_model = SelfModel()
        w_model = WorldModel()
        integrator = Integrator()

        s_emb = s_model.reflect(torch.randn((1,256)))
        w_emb = w_model.reason_about_world(torch.randn((1,256)))
        c = integrator.integrate(s_emb, w_emb)
        self.assertEqual(c.shape, s_emb.shape)
