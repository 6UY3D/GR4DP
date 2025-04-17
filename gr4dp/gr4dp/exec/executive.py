import threading
import time
import torch

class Executive:
    def __init__(self, ledger, self_model, world_model, integrator):
        self.ledger = ledger
        self.self_model = self_model
        self.world_model = world_model
        self.integrator = integrator
        self.running = False
        self.thread = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._main_loop, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _main_loop(self):
        while self.running:
            internal_state = torch.randn((1, 256))
            external_data = torch.randn((1, 256))
            s_emb = self.self_model.reflect(internal_state)
            w_emb = self.world_model.reason_about_world(external_data)
            c = self.integrator.integrate(s_emb, w_emb)
            self.integrator.update_ledger_memory(self.ledger, s_emb, w_emb, c)
            time.sleep(5)
