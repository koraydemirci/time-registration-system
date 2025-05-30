from fastapi.testclient import TestClient
from main import app
import uuid
import random

client = TestClient(app)

def test_full_flow():
    #generate random data
    random_suffix= uuid.uuid4().hex[:8]
    random_employer_name = f"employer_{random_suffix}"
    random_employer_email=f"{random_employer_name}@example.com"

    #1.Employer signup
    employer_signup = {
        "name": random_employer_name,
        "email": random_employer_email,
        "password": "testpassword",
        "user_type": "employer"
    }
    resp = client.post("/auth/signup", json=employer_signup)
    print(resp.status_code, resp.json())
    assert resp.status_code in (200, 201)
    employer_id = resp.json().get("user_id") 

    
    # 2. Employer login
    login_data = {
        "username": random_employer_email,
        "password": "testpassword"
    }
    resp = client.post("/auth/login", json=login_data)
    assert resp.status_code == 200
    token = resp.json().get("access_token")
    assert token
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Add customer
    customer_email = f"customer_{uuid.uuid4().hex[:8]}@example.com"
    customer_data = {
        "name": "Test Customer",
        "email": customer_email
    }
    resp = client.post("/customers/", json=customer_data, headers=headers)
    assert resp.status_code in (200, 201)
    customer_id = resp.json()["id"]
    
    # 4. Create project for customer
    project_data = {
        "name": "Test Project",
        "description": "A test project",
        "start_date": "2025-06-01T09:00:00",
        "end_date": "2025-07-01T17:00:00",
        "budget": 1000,
        "status": "active",
        "hour_rate": 50,
        "customer_id": customer_id,
        #"employer_id": employer_id  # Use the employer_id from signup
    }
    resp = client.post("/projects/", json=project_data, headers=headers)
    assert resp.status_code in (200, 201)
    assert resp.json()["name"] == "Test Project"
