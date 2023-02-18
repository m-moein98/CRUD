from main import app
from fastapi.testclient import TestClient


client = TestClient(app)
_id = None


def test_create_one():
    response = client.post(
        "api/", json={"name": "test", "description": "test description"}
    )
    global _id
    _id = response.json()
    assert response.status_code == 200


def test_get_one():
    response = client.get(f"api/{_id}")
    assert response.json()["_id"] == _id
    assert response.status_code == 200


def test_get_all():
    response = client.get("api/")
    assert _id in [item["_id"] for item in response.json()]
    assert response.status_code == 200


def test_update_one():
    response = client.patch(
        f"api/{_id}", json={"name": "test", "description": "test description"}
    )
    assert response.status_code == 200


def test_delete_one():
    response = client.delete(f"api/{_id}")
    assert response.status_code == 200
