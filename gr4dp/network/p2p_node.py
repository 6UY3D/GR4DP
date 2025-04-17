import threading
import socket
import logging
from gr4dp.network.peer_manager import PeerManager
from gr4dp.network.messages import handle_incoming_message

class P2PNode:
    def __init__(self, ledger, host="0.0.0.0", port=4000):
        self.ledger = ledger
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
        self.peers = PeerManager()
        self.logger = logging.getLogger("p2p_node")

    def start(self):
        self.running = True
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(10)
        self.server_socket.settimeout(2.0)
        threading.Thread(target=self._listen_for_connections, daemon=True).start()
        self.logger.info(f"P2P node started on {self.host}:{self.port}")

    def stop(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        self.logger.info("P2P node stopped.")

    def _listen_for_connections(self):
        while self.running:
            try:
                conn, addr = self.server_socket.accept()
                self.peers.add_peer(addr)
                threading.Thread(
                    target=self._handle_connection, args=(conn, addr), daemon=True
                ).start()
            except socket.timeout:
                pass

    def _handle_connection(self, conn, addr):
        with conn:
            data = conn.recv(4096)
            if not data:
                return
            message = data.decode("utf-8")
            handle_incoming_message(message, addr, self.ledger, self.logger)
