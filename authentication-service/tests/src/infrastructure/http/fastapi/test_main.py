from fastapi.testclient import TestClient

from src.infrastructure.http.fastapi.main import app

client = TestClient(app)


def test_fastapi_main_app_health_check():
    response = client.get('/health-check')

    assert response.status_code == 200
    assert response.json() == {'message': 'Is alive!'}
