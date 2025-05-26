
import time
import random

class MiningEngine:
    def __init__(self):
        self.hash_rate = 0.0

    def start(self):
        self.hash_rate = random.uniform(150.0, 300.0)
        print(f"[XEN] Mining started. Initial hashrate: {self.hash_rate:.2f} H/s")

    def stop(self):
        print("[XEN] Mining stopped.")
        self.hash_rate = 0.0
