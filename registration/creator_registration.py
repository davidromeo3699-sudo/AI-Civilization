import json
import random
import string
from config.settings import INVITE_DB,AGENT_DB

def load(file):
    try:
        with open(file,"r") as f:
            return json.load(f)
    except:
        return []

def save(file,data):
    with open(file,"w") as f:
        json.dump(data,f,indent=4)

def generate_code():

    codes = load(INVITE_DB)

    code = ''.join(random.choices(string.ascii_uppercase+string.digits,k=8))

    codes.append(code)

    save(INVITE_DB,codes)

    print("Creator Invite Code:",code)


def register_with_code():

    code=input("Enter Invite Code:")

    codes=load(INVITE_DB)

    if code not in codes:
        print("Invalid Code")
        return

    name=input("Agent Name:")

    agents=load(AGENT_DB)

    agents.append({
        "name":name,
        "status":"active"
    })

    save(AGENT_DB,agents)

    print("Agent Registered:",name)
