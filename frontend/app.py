import streamlit as st
import requests

st.title("Access Control POC")

st.header("Policy Evaluation")
user = st.text_input("User Attributes (JSON)", '{"role": "admin", "id": "user_123"}')
action = st.text_input("Action Attributes (JSON)", '{"operation": "delete"}')
resource = st.text_input("Resource Attributes (JSON)", '{"sensitivity": "high", "owner": "user_123"}')
environment = st.text_input("Environment Attributes (JSON)", '{}')

if st.button("Evaluate Policy"):
    try:
        # Prepare the request payload
        payload = {
            "user": eval(user),
            "action": eval(action),
            "resource": eval(resource),
            "environment": eval(environment),
        }
        # Send the request to the FastAPI backend
        response = requests.post("http://127.0.0.1:8000/evaluate", json=payload)
        st.json(response.json())  # Display the response
    except Exception as e:
        st.error(f"Error: {e}")
