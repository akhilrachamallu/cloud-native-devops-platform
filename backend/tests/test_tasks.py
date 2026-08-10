def create_test_user(client):
    response = client.post(
        "/api/users/",
        json={
            "email": "taskuser@example.com",
            "username": "taskuser",
            "password": "TestPassword123",
        },
    )

    assert response.status_code == 201


def get_auth_headers(client):
    response = client.post(
        "/api/auth/login",
        json={
            "email": "taskuser@example.com",
            "password": "TestPassword123",
        },
    )

    assert response.status_code == 200

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }


def test_tasks_require_authentication(client):
    response = client.get("/api/tasks/")

    assert response.status_code == 401


def test_create_task(client):
    create_test_user(client)

    headers = get_auth_headers(client)

    response = client.post(
        "/api/tasks/",
        headers=headers,
        json={
            "title": "Build CI/CD Pipeline",
            "description": "Implement GitHub Actions",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Build CI/CD Pipeline"
    assert data["description"] == "Implement GitHub Actions"
    assert data["status"] == "pending"
    assert "user_id" in data


def test_get_tasks(client):
    create_test_user(client)

    headers = get_auth_headers(client)

    create_response = client.post(
        "/api/tasks/",
        headers=headers,
        json={
            "title": "Test Task",
            "description": "Test description",
        },
    )

    assert create_response.status_code == 201

    response = client.get(
        "/api/tasks/",
        headers=headers,
    )

    assert response.status_code == 200

    tasks = response.json()

    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test Task"


def test_update_task(client):
    create_test_user(client)

    headers = get_auth_headers(client)

    create_response = client.post(
        "/api/tasks/",
        headers=headers,
        json={
            "title": "Original Task",
            "description": "Original description",
        },
    )

    task_id = create_response.json()["id"]

    response = client.patch(
        f"/api/tasks/{task_id}",
        headers=headers,
        json={
            "title": "Updated Task",
            "status": "completed",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Updated Task"
    assert data["status"] == "completed"


def test_delete_task(client):
    create_test_user(client)

    headers = get_auth_headers(client)

    create_response = client.post(
        "/api/tasks/",
        headers=headers,
        json={
            "title": "Task to Delete",
            "description": "This task will be deleted",
        },
    )

    task_id = create_response.json()["id"]

    response = client.delete(
        f"/api/tasks/{task_id}",
        headers=headers,
    )

    assert response.status_code == 204

    get_response = client.get(
        f"/api/tasks/{task_id}",
        headers=headers,
    )

    assert get_response.status_code == 404