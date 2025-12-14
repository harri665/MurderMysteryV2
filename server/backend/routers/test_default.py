from fastapi.testclient import TestClient
from ..server import app

client = TestClient(app)

def test_default_get():
  response = client.get('/')
  assert response.status_code == 200
  assert response.json() == {'Hello': 'World'}
