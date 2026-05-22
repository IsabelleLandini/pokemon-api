import pytest
from app.services.pokemon_service import PokemonService
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_get_pokemons():
    service = PokemonService()

    #Mock da lista
    service.client.get_pokemons = AsyncMock(return_value={
        'count': 2,
        'next': 'next_url',
        'previous': None,
        'results': [
            {'name': 'pikachu'},
            {'name': 'bulbasaur'}
        ]
    })

# Mock dos detalhes
    async def mock_get_pokemon(name):
        return {
            'id': 1 if name == 'pikachu' else 2,
            'name': name,
            'height': 10,
            'weight': 100,
            'types': [{'type': {'name': 'eletric'}}],
            'sprites': {
                'front_default': 'url_front',
                'back_default': 'url_back'
        }
    }

    service.client.get_pokemon = mock_get_pokemon     
     
    result = await service.get_pokemons(limit=2, offset=0)

    # Validações
    assert len(result['data']) == 2
    assert result['pagination']['limit'] == 2
    assert result['pagination']['offset'] == 0
    assert result['pagination']['total'] == 2

    assert result['data'][0]['name'] == 'pikachu'
    assert result['data'][1]['name'] == 'bulbasaur'

