from fastapi import FastAPI
from app.attributes import ATTRIBUTES
import requests
from pydantic import BaseModel
from app.evaluate import RequestContext, evaluate_policy

app = FastAPI()

@app.post("/evaluate")
def evaluate(context: RequestContext):
    """
    Evaluate the request using OPA.
    """
    return evaluate_policy(context)


def load_policies():
    with open("app/policies.rego", "r") as file:
        policies = file.read()
    response = requests.put(
        "http://localhost:8181/v1/policies/poc-policy",  # OPA API endpoint
        data=policies
    )
    if response.status_code == 200:
        print("Policies loaded successfully")
    else:
        print(f"Failed to load policies: {response.text}")

# Load policies on application startup
load_policies()

@app.get("/")
def read_root():
    return {"message": "Access Control POC is running"}

@app.get("/attributes")
def get_attributes():
    return {"attributes": ATTRIBUTES}


