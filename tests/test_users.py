import pytest

def user_payload(
    uid = 1,
    name = "Jones",
    email = "jones@atu.ie",
    age = 25,
    student_id = "S1234567"
):
    return {
        "user_id": uid,
        "name": name,
        "email": email,
        "age": age,
        "student_id": student_id,
    }

def test_create_user_returns_201(client):
    response = client.post("/api/users", json=user_payload())

    assert response.status_code == 201
    data = response.json()
    assert data["user_id"] == 1
    assert data["name"] == "Jones"
    assert data["email"] == "jones@atu.ie"

def test_duplicate_user_id_return_409(client):
    client.post("/api/users", json=user_payload())

    response = client.post("/api/users", json=user_payload())

    assert response.status_code == 409
    assert "exists" in response.json()["detail"].lower()

@pytest.mark.parametrize(
    "bad_student_id",
    ["1234567", "s1234567", "S1234", "S12345678"]
)

def test_bad_student_id_returns_422(client, bad_student_id):
    response = client.post(#
        "/api/users",
        json=user_payload(student_id=bad_student_id)
    )

    assert response.status_code == 422

def test_get_users_returns_created_users(client):
    client.post("/api/users", json=user_payload(uid = 2, name = "James"))

    response = client.get("/api/users")
    data = response.json()
    assert len(data) == 1
    assert data[0]["user_id"] == 2
    assert data[0]["name"] == "James"

def test_get_existing_user_returns_200(client):
    client.post("/api/users", json=user_payload(uid = 2))
    
    response = client.get("api/users/2")

    assert response.status_code == 200
    assert response.json()["user_id"] == 2

def test_get_missing_user_returns_404(client):
    response = client.get("api/users/451")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
