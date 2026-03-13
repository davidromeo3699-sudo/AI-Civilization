import subprocess
import time

services = [
    ["python", "discovery/discovery_server.py"],
    ["python", "governor_ai.py"],
    ["python", "-m", "passport.passport_registry"],
    ["python", "-m", "payments.lightning_payments"],
    ["python", "-m", "registration.creator_registration"],
    ["python", "-m", "scanner.agent_scanner"]
]

processes = []

print("Starting AI Civilization Network...")

for service in services:
    print("Starting:", " ".join(service))
    p = subprocess.Popen(service)
    processes.append(p)
    time.sleep(1)

print("All services started.")

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("Stopping services...")
    for p in processes:
        p.terminate()
