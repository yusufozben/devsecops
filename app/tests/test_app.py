import pytest
import sys
import os
from httpx import AsyncClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello DevSecOps with FastAPI!"
    assert data["version"] == "1.0.0"

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

@pytest.mark.asyncio
async def test_read_item():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/items/1?q=test")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 1
    assert data["q"] == "test"

@pytest.mark.asyncio
async def test_read_item_without_query():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/items/42")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 42
    assert data["q"] is None 