import pytest

@pytest.mark.asyncio
async def test_get_pokemons(client):
    response = await client.get('/pokemons?limit=10&offset=0')

    assert response.status_code == 200

    data = response.json()

    assert 'data' in data
    assert 'pagination' in data
    assert isinstance(data['data'][0], list)
    assert len(data['data']) > 0
    assert 'name' in data['data'][0]

@pytest.mark.asyncio
async def test_get_pokemons_with_pagination(client):
    response = await client.get('/pokemons?limit=5&offset=0')

    assert response.status_code == 200

    data = response.json()

    assert len(data['data']) == 5
    assert data['pagination']['limit'] == 5
    assert data['pagination']['offset'] == 0
    assert 'total' in data['pagination']

@pytest.mark.asyncio
async def test_get_pokemon(client):
    response = await client.get('/pokemons/pikachu')

    assert response.status_code == 200

    data = response.json()

    assert data['name'] == 'pikachu'
    assert 'id' in data
    assert 'types' in data

@pytest.mark.asyncio
async def test_get_pokemon_not_found(client):
    response = await client.get('/pokemons/pokemon-inexistente')

    assert response.status_code == 404

    data = response.json()
    assert 'detail' in data

    
