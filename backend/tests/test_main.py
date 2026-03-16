import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool


from db.database import Base

# Fixing Database connections (Force to Connect SqlLite Memory)
with patch.object(Base.metadata, "create_all"):
    from dependencies import get_db
    from main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# TEST CASES


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Test Task", "description": "This is a test"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test"
    assert data["is_completed"] is False
    assert "id" in data


def test_get_tasks_filters_completed_and_limits_to_five():
    for i in range(1, 7):
        client.post("/tasks", json={"title": f"Task {i}"})

    res = client.post("/tasks", json={"title": "Done Task"})
    task_id = res.json()["id"]
    client.patch(f"/tasks/{task_id}/done")

    # Fetch Tasks
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()

    assert len(data) == 5

    # Not Completed
    titles = [task["title"] for task in data]
    assert "Done Task" not in titles

    # Verify order
    assert data[0]["title"] == "Task 6"
    assert data[4]["title"] == "Task 2"


def test_mark_task_done():
    # Creating a task
    create_res = client.post("/tasks", json={"title": "Task to complete"})
    task_id = create_res.json()["id"]

    # Mark task done
    patch_res = client.patch(f"/tasks/{task_id}/done")
    assert patch_res.status_code == 200
    assert patch_res.json()["is_completed"] is True

    # Check no completed task appears
    get_res = client.get("/tasks")
    data = get_res.json()
    assert len(data) == 0

# invalid task check


def test_mark_nonexistent_task_done():
    response = client.patch("/tasks/999/done")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"
