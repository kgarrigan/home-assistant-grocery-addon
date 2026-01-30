from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

# Print paths for debugging
print("Current working directory:", Path.cwd())
print("__file__ path:", Path(__file__).resolve())
print("Attempting data file at:", Path(__file__).parent / "run" / "data.json")

DATA_FILE = Path(__file__).parent / "run" / "data.json"

def read_checklist():
    print("Reading checklist from:", DATA_FILE.resolve())
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_checklist(data):
    print("Writing checklist to:", DATA_FILE.resolve())
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
