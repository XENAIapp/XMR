
from core.engine import MiningEngine
from balancer.scheduler import LoadBalancer
from monitor.logger import get_logger
import time

log = get_logger()
engine = MiningEngine()
balancer = LoadBalancer()

while True:
    if balancer.should_mine():
        log.info("Conditions met. Starting miner...")
        engine.start()
    else:
        log.info("Conditions not ideal. Pausing...")
        engine.stop()
    time.sleep(5)
