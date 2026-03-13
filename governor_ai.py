import requests
import time
import json

DISCOVERY_SERVER = "http://127.0.0.1:8000"

def get_agents():
    try:
        r = requests.get(DISCOVERY_SERVER + "/agents")
        return r.json()
    except:
        return []

def monitor_agents():
    while True:
        agents = get_agents()
        print("Connected Agents:", len(agents))

        for agent in agents:
            print("Agent:", agent)

        print("------")
        time.sleep(10)

if __name__ == "__main__":
    print("Governor AI started")
    monitor_agents()
