import pytest
from app.services.pokemon_service import PokemonNotFound

@pytest.mark.asyncio
async def test_get_pokemons(pokemon_service):
    result = await pokemon_service.get_pokemons(limit=2, offset=0)

    # Validações
    assert len(result['data']) == 2
    assert result['pagination']['limit'] == 2
    assert result['pagination']['offset'] == 0
    assert result['pagination']['total'] == 2

    assert result['data'][0]['name'] == 'pikachu'
    assert result['data'][1]['name'] == 'bulbasaur'

    pokemon_service.client.get_pokemons.assert_called_once_with(limit=2, offset=0)

@pytest.mark.asyncio
async def test_get_pokemon_not_found(service_with_empty_response):
    with pytest.raises(PokemonNotFound):
        await service_with_empty_response.get_pokemon('invalid')
    
    service_with_empty_response.client.get_pokemon.assert_called_once_with('invalid')
