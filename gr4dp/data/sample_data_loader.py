import torch
from torch.utils.data import Dataset, DataLoader
import random

class SampleDataset(Dataset):
    def __init__(self, size=1000):
        self.size = size
        self.data = []
        for _ in range(size):
            x = torch.randn(256)
            y = x * random.uniform(0.8, 1.2)
            self.data.append((x, y))

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.data[idx]

def get_sample_dataloader(batch_size=32):
    dataset = SampleDataset()
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)
