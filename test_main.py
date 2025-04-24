from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_dna_sequences():
    response = client.get("/dna_sequences")
    assert response.status_code == 200
    assert "sequences" in response.json()
