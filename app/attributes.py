# app/attributes.py

ATTRIBUTES = {
    "user": {
        "role": "string",  # User's role (e.g., admin, viewer)
        "id": "string"     # Unique user identifier
    },
    "action": {
        "operation": "string"  # Action type (e.g., read, write, delete)
    },
    "resource": {
        "sensitivity": "string",  # Sensitivity level (e.g., low, high)
        "owner": "string"         # Owner's ID
    },
    "environment": {
        "time_of_day": "string",  # Time of day (e.g., "14:30")
        "location": "string"      # Location or IP address
    }
}
