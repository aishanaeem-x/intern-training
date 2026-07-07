import json
import os

def save(filename,data):
    with open(filename,"w") as f:
        json.dump(data,f,indent=4)

def load(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return None