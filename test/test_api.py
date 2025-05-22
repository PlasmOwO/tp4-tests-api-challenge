import requests

BASE_URL = "http://127.0.0.1:5000"

def test_create_user():
    res = requests.post(f"{BASE_URL}/users", json={"name": "Alice"})
    assert res.status_code == 201
    assert "id" in res.json()

def test_get_all_users():
    res = requests.get(f"{BASE_URL}/users")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_user_by_id():
    id = requests.post(f"{BASE_URL}/users", json={"name": "Antoine"}).json().get("id")
    res = requests.get(f"{BASE_URL}/users/{id}")
    assert res.status_code == 200

def test_delete_user():
    id = requests.post(f"{BASE_URL}/users", json={"name": "Patrick"}).json().get("id")
    res =requests.delete(f"{BASE_URL}/users/{id}")
    assert res.status_code == 204

def test_delete_non_existing_user():
    res = requests.delete(f"{BASE_URL}/users/999")
    assert res.status_code == 404

def test_create_empty_user():
    res = requests.post(f"{BASE_URL}/users", json={})
    assert res.status_code == 400

# TODO: test_get_user_by_id
# TODO: test_delete_user

