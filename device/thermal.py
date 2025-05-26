
import psutil

def check_temperature():
    try:
        temps = psutil.sensors_temperatures()
        cpu_temps = temps.get("coretemp", [])
        if cpu_temps:
            return max([t.current for t in cpu_temps])
        return None
    except Exception:
        return None
