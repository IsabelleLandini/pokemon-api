import pytest
from app.services.pokemon_service import PokemonService
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_get_pokemon():
    service = PokemonService()

    # Mock da resposta da API
    service.client.get_pokemon = AsyncMock(return_value={
        'id': 25,
        'name': 'pikachu',
        'height': 4,
        'weight': 60,
        'types': [{'type': {'name': 'eletric'}}],
        'sprites': {
            'front_default': 'url_front',
            'back_default': 'url_back'
        },
        'stats': [
            {'stat': {'name': 'speed'}, 'base_stat': 90}    
        ]    
    })

    result = await service.get_pokemon('pikachu')

    assert result['name'] == 'pikachu'
    assert 'eletric' in result['types']
    