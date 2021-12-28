import pytest
from fastapi.testclient import TestClient


@pytest.mark.fastapi
@pytest.mark.asyncio
async def test_fastapi_main_app_health_check(fastapi_client: TestClient):
    response = fastapi_client.get('/health-check')

    assert response.status_code == 200
    assert response.json() == {'message': 'Is alive!'}
