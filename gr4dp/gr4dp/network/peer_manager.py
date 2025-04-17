import threading

class PeerManager:
    def __init__(self):
        self.peers = []
        self.lock = threading.Lock()

    def add_peer(self, addr):
        with self.lock:
            if addr not in self.peers:
                self.peers.append(addr)

    def remove_peer(self, addr):
        with self.lock:
            if addr in self.peers:
                self.peers.remove(addr)

    def list_peers(self):
        with self.lock:
            return list(self.peers)
