import torch
import torch.nn as nn

class SelfModel(nn.Module):
    def __init__(self, input_dim=256, hidden_dim=512, output_dim=256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )

    def forward(self, x):
        return self.net(x)

    def reflect(self, internal_state):
        with torch.no_grad():
            return self.forward(internal_state)
