def handle_incoming_message(message, addr, ledger, logger):
    logger.info(f"Incoming message from {addr}: {message}")

    if message.startswith("request_latest_block"):
        latest = ledger.get_latest_block()
        logger.info(f"Responding to {addr} with latest block {latest}")
        # In real usage, you would send data back to the socket.
    elif message.startswith("new_block:"):
        pass
    else:
        logger.info("Unknown message type received.")
