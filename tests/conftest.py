import os

os.environ['API_KEY'] = 'pokemon123'

import pytest
import pytest_asyncio
from unittest.mock import AsyncMock
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.services.pokemon_service import PokemonService
from app.core.database import Base, engine

@pytest.fixture(autouse=True)
def clean_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

# HTTP Client 
@pytest_asyncio.fixture(scope='function')
async def client():
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

# Mock Data
@pytest.fixture
def pokemon_list_response():
    return {
        'count': 2,
        'next': 'next_url',
        'previous': None,
        'results': [
            {'name': 'pikachu'},
            {'name': 'bulbasaur'}
        ]    
    }

@pytest.fixture
def pokemon_detail_factory():
    def _factory(name: str):
        return {
            'id': 1 if name == 'pikachu' else 2,
            'name': name,
            'height': 10,
            'weight': 100,
            'types': [{'type': {'name': 'electric'}}],
            'sprites': {
                'front_default': 'url_front',
                'back_default': 'url_back'
            },
            'stats': [
            {
                'stat': {'name': 'speed'},
                'base_stat': 90
            },
            {
                'stat': {'name': 'attack'},
                'base_stat': 55
            }
        ]
    }
    return _factory

# Service
@pytest.fixture
def pokemon_service(pokemon_list_response, pokemon_detail_factory):
    svc = PokemonService()

    svc.client.get_pokemons = AsyncMock(return_value=pokemon_list_response)
    svc.client.get_pokemon = AsyncMock(side_effect=pokemon_detail_factory)

    return svc

@pytest.fixture
def service_with_empty_response(pokemon_service):
    pokemon_service.client.get_pokemon= AsyncMock(return_value=None)
   
    return pokemon_service

@pytest.fixture(autouse=True)
def mock_redis(monkeypatch):
    mock = AsyncMock()

    mock.get.return_value = None
    mock.set.return_value = True

    monkeypatch.setattr('app.services.pokemon_service.redis_client', mock)
