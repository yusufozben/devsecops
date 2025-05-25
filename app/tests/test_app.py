import pytest
import sys
import os
from httpx import AsyncClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app


@pytest.mark.asyncio
async def test_sum_two_numbers():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/sum?a=3&b=5")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    data = response.json()
    assert data["result"] == 7, f"Unexpected sum result: {data['result']}" # TODO: 3- assert error
