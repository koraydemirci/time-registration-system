from fastapi.testclient import TestClient
from main import app
from datetime import datetime, timedelta

client = TestClient(app)

def test_create_timeblock():
    payload = {
        "start_date": (datetime.now() - timedelta(hours=2)).isoformat(),
        "end_date": datetime.now().isoformat(),
        "note": "Unit test",
        "hours": 2.0,
        "project_id": 1,
        "employee_id": 1
    }
    response = client.post("/timeblocks/", json=payload)
    assert response.status_code in (200, 201)
    assert response.json()["note"] == "Unit test"

def test_get_timeblocks_by_employee():
    response = client.get("/timeblocks/employee/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_timeblocks_by_project():
    response = client.get("/timeblocks/project/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_timeblock():
    # Create first
    payload = {
        "start_date": (datetime.now() - timedelta(hours=3)).isoformat(),
        "end_date": datetime.now().isoformat(),
        "note": "Before update",
        "hours": 3.0,
        "project_id": 1,
        "employee_id": 1
    }
    create_resp = client.post("/timeblocks/", json=payload)
    tb_id = create_resp.json()["id"]
    # Update
    payload["note"] = "After update"
    update_resp = client.put(f"/timeblocks/{tb_id}", json=payload)
    assert update_resp.status_code == 200
    assert update_resp.json()["note"] == "After update"