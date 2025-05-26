
import psutil
import platform

class DeviceAgent:
    def get_status(self):
        battery = psutil.sensors_battery()
        return {
            "cpu": psutil.cpu_percent(interval=1),
            "charging": battery.power_plugged if battery else None,
            "platform": platform.system()
        }
