import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

HEADERS = { "x-api-key": "pokemon123"}

@pytest.mark.asyncio
async def test_create_pokemon():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url='http://test') as ac:

        payload = {
            'pokemon_id': 999,
            'name': 'testmon',
            'height': 10,
            'weight': 100,
            'types': 'fire',
            'front_sprite': 'url_front',
            'back_sprite': 'url_back'
        }

        response = await ac.post(
            '/pokemons/', 
            json=payload,
            headers=HEADERS
        )

        assert response.status_code == 200
        assert response.json()['name'] == 'testmon'