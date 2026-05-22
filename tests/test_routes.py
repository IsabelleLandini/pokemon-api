from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_pokemons():
    response = client.get('/pokemons')

    assert response.status_code == 200

    data = response.json()

    assert 'data' in data
    assert 'pagination' in data

def test_get_pokemons_with_pagination():
    response = client.get(
        '/pokemons?limit=5&offset=0'
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data['data']) == 5
    assert data['pagination']['limit'] == 5
    assert data['pagination']['offset'] == 0
