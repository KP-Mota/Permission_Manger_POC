import requests
from pydantic import BaseModel

class RequestContext(BaseModel):
    user: dict
    action: dict
    resource: dict
    environment: dict

def evaluate_policy(context: RequestContext):
    """
    Sends input to OPA for policy evaluation and returns the decision.
    """
    try:
        response = requests.post(
            "http://localhost:8181/v1/data/poc/access/allow",
            json={"input": context.dict()},
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
