import torch

def prepare_input(size=256):
    return torch.randn((1, size))

def device_info():
    return "cuda" if torch.cuda.is_available() else "cpu"
