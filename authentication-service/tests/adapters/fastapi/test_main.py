from fastapi.testclient import TestClient

from service.adapters.fastapi.main import app

client = TestClient(app)


def test_adapters_fastapi_main_app_health_check():
    response = client.get('/health-check')

    assert response.status_code == 200
    assert response.json() == {'message': 'Is alive!'}