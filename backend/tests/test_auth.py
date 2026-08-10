def test_register_user(client):
    response = client.post(
        "/api/users/",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "TestPassword123",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["email"] == "test@example.com"
    assert data["username"] == "testuser"
    assert "password" not in data
    assert "hashed_password" not in data


def test_login_user(client):
    register_response = client.post(
        "/api/users/",
        json={
            "email": "login@example.com",
            "username": "loginuser",
            "password": "TestPassword123",
        },
    )

    assert register_response.status_code == 201

    login_response = client.post(
        "/api/auth/login",
        json={
            "email": "login@example.com",
            "password": "TestPassword123",
        },
    )

    assert login_response.status_code == 200

    data = login_response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"