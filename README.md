# Permission_Manger_POC
Build and develop a permission manager service for access control.

We begin with sprint one implementing primitive ABAC and using OPA for access control.

# Access Control POC

## **Project Overview**
This project is a Proof of Concept (POC) implementation of a dynamic access control system using **FastAPI** and **Open Policy Agent (OPA)**. The system evaluates access policies for users, actions, resources, and environmental conditions. It is designed to handle complex, modular policies and provides a user-friendly interface for testing.

## **Key Features**
1. **Policy-Based Access Control**:
   - Implemented Attribute-Based Access Control (ABAC) with Rego policies in OPA.
   - Modular policy definitions that support dynamic evaluation based on user inputs.

2. **Backend API**:
   - A FastAPI backend with a `/evaluate` endpoint that interacts with OPA for policy evaluation.
   - Modular structure with separate components for policy management and evaluation.

3. **Streamlit Frontend**:
   - A simple and interactive frontend for testing access control scenarios.
   - Allows users to input custom attributes for users, actions, resources, and environments.
   - Displays real-time policy evaluation results.

4. **Policy Examples**:
   - Policies to manage resource access based on roles, ownership, and sensitivity levels.
   - Support for common operations like `read`, `delete`, and `update`.

## **Implemented Features**
- **OPA Integration**:
  - Deployed OPA using Docker and integrated it with the FastAPI backend.
  - Successfully loaded and tested Rego policies.

- **Policy Evaluation**:
  - Defined policies for scenarios like:
    - Admin accessing sensitive resources.
    - Users accessing their own resources.
    - Unauthorized users attempting restricted operations.

- **Frontend Integration**:
  - Streamlit app for manual testing of policy evaluation.
  - Dynamic JSON input fields for flexibility.

## **Folder Structure**
```
Permission_Manger_POC/
├── app/
│   ├── __init__.py       # Marks app as a package
│   ├── main.py           # FastAPI backend entry point
│   ├── evaluate.py       # Handles policy evaluation logic
│   ├── policies.rego     # Rego policies
├── frontend/
│   ├── app.py            # Streamlit app for frontend testing
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── environment.yml       # Conda environment configuration (optional)
```

## **How to Run the Project**

### Prerequisites
1. Install **Docker** to run OPA.
2. Install **Miniconda** or **Python 3.9+**.
3. Install dependencies using `pip` or `conda`.

### Steps to Run

#### **1. Start OPA**
- Run OPA using Docker:
  ```bash
  docker run -d -p 8181:8181 openpolicyagent/opa:latest run --server
  ```

#### **2. Start the FastAPI Backend**
- Activate the Conda environment:
  ```bash
  conda activate access-control-poc
  ```
- Start the backend server:
  ```bash
  uvicorn app.main:app --reload
  ```

#### **3. Run the Streamlit Frontend**
- Start the frontend application:
  ```bash
  streamlit run frontend/app.py
  ```
- Open the URL displayed in the terminal (e.g., `http://localhost:8501`).

## **Example Policy**
```rego
package poc.access

default allow = false

# Allow delete operation for high sensitivity resources by admin users
allow {
    input.resource.sensitivity == "high"
    input.action.operation == "delete"
    input.user.role == "admin"
}

# Allow resource access if the user is the owner
allow {
    input.resource.owner == input.user.id
}
```

## **Planned Improvements**
1. **Dynamic Policy Updates**:
   - Integrate OPAL for real-time policy updates.

2. **Enhanced Frontend**:
   - Add predefined templates for common policy scenarios.
   - Include visualizations for policy decision-making.

3. **Advanced Policy Features**:
   - Support for more complex conditions and multi-attribute constraints.
   - Implement policy versioning.

4. **Error Logging and Analytics**:
   - Add detailed logging for all policy evaluation requests.
   - Include analytics for tracking policy usage.

## **Contributors**
- Kaivalya Pandit

## **License**
This project is licensed under the MIT License.




