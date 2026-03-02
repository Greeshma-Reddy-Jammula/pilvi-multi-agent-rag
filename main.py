from fastapi import FastAPI, Query
import random

app = FastAPI()

# Mock planner + executor
def planner(task: str):
    return f"Analyze: {task}"

def executor(task: str):
    return f"Execute: {task}"

@app.post("/orchestrate/")
def orchestrate(task: str = Query(...)):
    return {"plan": planner(task), "result": executor(task)}

# Mock A/B models
def model_a(input_text: str):
    return f"Model A response: {input_text}"

def model_b(input_text: str):
    return f"Model B response: {input_text}"

@app.get("/predict/")
def predict(input_text: str, user_id: int = Query(None)):
    if user_id is not None and user_id % 10 == 0:
        chosen = "B"
    else:
        chosen = "A"
    response = model_a(input_text) if chosen == "A" else model_b(input_text)
    return {"model": chosen, "response": response}
