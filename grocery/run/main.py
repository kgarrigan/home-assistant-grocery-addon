from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

# Path to JSON file (relative to main.py)
DATA_FILE = "/app/data.json"

# Helper functions
def read_checklist():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_checklist(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# GET endpoint — read checklist
@app.get("/checklist")
def get_checklist():
    return read_checklist()

# POST endpoint — add a new item
@app.post("/checklist")
def add_item(item: dict):
    data = read_checklist()
    data["checklist"].append(item)
    write_checklist(data)
    return {"status": "success", "checklist": data["checklist"]}
