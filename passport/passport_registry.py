import json
import uuid
from config.settings import PASSPORT_DB

def load():
    try:
        with open(PASSPORT_DB,"r") as f:
            return json.load(f)
    except:
        return []

def save(data):
    with open(PASSPORT_DB,"w") as f:
        json.dump(data,f,indent=4)

def create_passport(agent):

    passports=load()

    passport={
        "agent":agent,
        "id":str(uuid.uuid4()),
        "reputation":0
    }

    passports.append(passport)

    save(passports)

    print("Passport created for",agent)
