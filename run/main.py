from fastapi import FastAPI

app = FastAPI()

@app.get("/checklist")
def get_checklist():
    return {
        "checklist": [
            "Milk",
            "Eggs",
            "Bread"
        ]
    }
