import os

def verify_plot(plot_path):
    return os.path.exists(plot_path) and os.path.getsize(plot_path) > 0

def create_plot(plot_path, size_gb=1):
    with open(plot_path, "wb") as f:
        f.seek(size_gb * 1024 * 1024 * 1024 - 1)
        f.write(b"\0")
    return True
