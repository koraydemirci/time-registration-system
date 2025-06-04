from fastapi.testclient import TestClient
from main import app
from datetime import datetime, timedelta

client = TestClient(app)

def get_auth_headers():
    # Create a unique employer and login to get a token
    import uuid
    email = f"employer_{uuid.uuid4().hex[:8]}@example.com"
    signup = {
        "name": "Test Employer",
        "email": email,
        "password": "testpassword",
        "user_type": "employer"
    }
    client.post("/auth/signup", json=signup)
    login = {
        "username": email,
        "password": "testpassword"
    }
    resp = client.post("/auth/login", data=login)
    token = resp.json().get("access_token")
    return {"Authorization": f"Bearer {token}"}

def test_create_project():
    headers = get_auth_headers()
    # Create a customer first
    customer_data = {
        "name": "Customer1",
        "email": f"customer_{datetime.now().timestamp()}@example.com"
    }
    resp = client.post("/customers/", json=customer_data, headers=headers)
    assert resp.status_code in (200, 201)
    customer_id = resp.json()["id"]

    project_data = {
        "name": "Test Project",
        "description": "A test project",
        "start_date": (datetime.now() - timedelta(days=1)).isoformat(),
        "end_date": (datetime.now() + timedelta(days=10)).isoformat(),
        "budget": 1000,
        "status": "active",
        "hour_rate": 50,
        "customer_id": customer_id
    }
    resp = client.post("/projects/", json=project_data, headers=headers)
    assert resp.status_code in (200, 201)
    assert resp.json()["name"] == "Test Project"

def test_get_projects():
    resp = client.get("/projects/")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_get_project_by_id():
    resp = client.get("/projects/")
    assert resp.status_code == 200
    projects = resp.json()
    if projects:
        project_id = projects[0]["id"]
        resp2 = client.get(f"/projects/{project_id}")
        assert resp2.status_code == 200
        assert resp2.json()["id"] == project_id



def test_assign_employee_to_project():
    headers = get_auth_headers()
    # Create a customer
    customer_data = {
        "name": "Customer2",
        "email": f"customer_{datetime.now().timestamp()}@example.com"
    }
    resp = client.post("/customers/", json=customer_data, headers=headers)
    customer_id = resp.json()["id"]

    # Create a project
    project_data = {
        "name": "Project Assign",
        "description": "Assign test",
        "start_date": (datetime.now() - timedelta(days=1)).isoformat(),
        "end_date": (datetime.now() + timedelta(days=5)).isoformat(),
        "budget": 500,
        "status": "active",
        "hour_rate": 30,
        "customer_id": customer_id
    }
    resp = client.post("/projects/", json=project_data, headers=headers)
    project_id = resp.json()["id"]

    # Create an employee
    import uuid
    emp_email = f"employee_{uuid.uuid4().hex[:8]}@example.com"
    emp_signup = {
        "name": "Test Employee",
        "email": emp_email,
        "password": "testpassword",
        "user_type": "employee"
    }
    client.post("/auth/signup", json=emp_signup)
    emp_login = {
        "username": emp_email,
        "password": "testpassword"
    }
    emp_resp = client.post("/auth/login", data=emp_login)
    employees_resp = client.get("/employees/")
    assert employees_resp.status_code == 200, employees_resp.text
    try:
        employees = employees_resp.json()
    except Exception:
        raise AssertionError(f"Response is not JSON: {employees_resp.text}")

    assert isinstance(employees, list), f"Expected list, got: {type(employees)} - {employees}"

    employee_id_list = [e["id"] for e in employees if e.get("email") == emp_email]
    assert employee_id_list, f"Employee with email {emp_email} not found in {employees}"
    employee_id = employee_id_list[0]

    # Assign employee to project
    assign_resp = client.post(f"/projects/{project_id}/assign?employee_id={employee_id}", headers=headers)
    assert assign_resp.status_code in (200, 201)
    # Optionally, check the response content
    assert "assigned" in assign_resp.text.lower() or assign_resp.json().get("id") == project_id