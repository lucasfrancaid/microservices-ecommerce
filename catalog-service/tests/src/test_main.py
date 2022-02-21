import pytest
from fastapi.testclient import TestClient

from src.main import app

test_client = TestClient(app)


@pytest.mark.fastapi
def test_main_fastapi_health_check():
    response = test_client.get('/health-check')

    assert response.status_code == 200
    assert response.json() == {'message': 'Is alive!'}
