import logging

def setup_logger():
    logging.basicConfig(
        filename="logs.txt",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )