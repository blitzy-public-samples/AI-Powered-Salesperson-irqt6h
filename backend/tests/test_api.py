import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import User, ChatSession, Quote
from app.database import get_db
from sqlalchemy.orm import Session

client = TestClient(app)

@pytest.fixture(scope="module")
def db():
    db = next(get_db())
    yield db
    db.close()

# Test authentication endpoints
def test_login(db: Session):
    response = client.post("/auth/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_register(db: Session):
    response = client.post("/auth/register", json={"username": "newuser", "email": "new@example.com", "password": "newpass"})
    assert response.status_code == 201
    assert "id" in response.json()

# Test chat session endpoints
def test_create_chat_session(db: Session):
    response = client.post("/chat/sessions", json={"name": "Test Session"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 201
    assert "id" in response.json()

def test_get_chat_sessions(db: Session):
    response = client.get("/chat/sessions", headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test quote generation endpoints
def test_generate_quote(db: Session):
    response = client.post("/quotes/generate", json={"prompt": "Test prompt"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 200
    assert "quote" in response.json()

def test_get_quotes(db: Session):
    response = client.get("/quotes", headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test user management endpoints
def test_get_user_profile(db: Session):
    response = client.get("/users/me", headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 200
    assert "username" in response.json()

def test_update_user_profile(db: Session):
    response = client.put("/users/me", json={"email": "updated@example.com"}, headers={"Authorization": "Bearer <token>"})
    assert response.status_code == 200
    assert response.json()["email"] == "updated@example.com"

# HUMAN ASSISTANCE NEEDED
# The following tests need to be expanded with more specific assertions and edge cases:
# - Test invalid login credentials
# - Test registering with existing username or email
# - Test creating chat session with invalid data
# - Test generating quote with empty prompt
# - Test updating user profile with invalid data