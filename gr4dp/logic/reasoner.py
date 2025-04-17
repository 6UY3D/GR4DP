class Reasoner:
    def __init__(self, theorem_prover, modal_logic_engine):
        self.theorem_prover = theorem_prover
        self.modal_logic_engine = modal_logic_engine

    def analyze(self, statement):
        proven, proof_steps = self.theorem_prover.prove(statement)
        modal_eval = self.modal_logic_engine.evaluate_modal_statement(statement)
        return proven, proof_steps, modal_eval
