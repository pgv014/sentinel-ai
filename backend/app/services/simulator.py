import random
import time
import requests

URL = "http://127.0.0.1:8000/telemetry"

devices = [
    "Cooling-01",
    "Cooling-02",
    "Pump-01",
    "Pump-02",
    "Motor-01",
    "Motor-02"
]

state = {}

for device in devices:
    state[device] = {
        "temperature": random.uniform(42, 48),
        "pressure": random.uniform(92, 98),
        "power": random.uniform(108, 118),
        "vibration": random.uniform(0.25, 0.40),
    }

counter = 0

while True:

    counter += 1

    failing_device = "Pump-02"

    for device in devices:

        s = state[device]

        if device == failing_device and counter > 40:
            s["temperature"] += random.uniform(0.2, 0.6)
            s["vibration"] += random.uniform(0.02, 0.05)
            s["power"] += random.uniform(0.5, 1.5)
            s["pressure"] -= random.uniform(0.1, 0.3)

        else:
            s["temperature"] += random.uniform(-0.2, 0.2)
            s["vibration"] += random.uniform(-0.01, 0.01)
            s["power"] += random.uniform(-0.5, 0.5)
            s["pressure"] += random.uniform(-0.2, 0.2)

        payload = {
            "device_name": device,
            "temperature": round(s["temperature"], 2),
            "vibration": round(s["vibration"], 2),
            "pressure": round(s["pressure"], 2),
            "power": round(s["power"], 2)
        }

        requests.post(URL, json=payload)

        print(payload)

    time.sleep(1)