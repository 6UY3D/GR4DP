import torch
import torch.optim as optim

def train_model(model, data_loader, epochs=1):
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = torch.nn.MSELoss()

    for epoch in range(epochs):
        for batch in data_loader:
            x, y = batch
            optimizer.zero_grad()
            output = model(x)
            loss = loss_fn(output, y)
            loss.backward()
            optimizer.step()
