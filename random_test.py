import requests

def authorize_user(user, action, resource, environment):
    # Construct the JSON query
    query = {
        "user": {
            "role": user.get("role"),
            "id": user.get("id"),
        },
        "action": {
            "method": action.get("method"),
            "endpoint": action.get("endpoint"),
        },
        "resource": {
            "type": resource.get("type"),
            "id": resource.get("id"),
        },
        "environment": environment
    }

    # Send query to OPA
    response = requests.post(
        "http://localhost:8181/v1/data/system/authz/allow",
        json={"input": query}
    )

    # Return the decision
    if response.status_code == 200:
        return response.json().get("result", False)
    else:
        raise Exception(f"OPA error: {response.text}")
