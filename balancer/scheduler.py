
from agents.device_agent import DeviceAgent

class LoadBalancer:
    def __init__(self):
        self.agent = DeviceAgent()

    def should_mine(self):
        status = self.agent.get_status()
        if status["charging"] and status["cpu"] < 20:
            return True
        return False
