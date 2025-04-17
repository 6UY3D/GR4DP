class TheoremProver:
    def __init__(self):
        self.axioms = ["AXIOM_1", "AXIOM_2"]

    def prove(self, statement):
        return True, ["SAMPLE_PROOF_STEP_1", "SAMPLE_PROOF_STEP_2"]

    def verify(self, statement, proof):
        return True
