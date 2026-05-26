from fastapi import APIRouter, Query, Depends

from app.core.security import verify_api_key
from app.schemas.pokemon import PokemonListResponse, PokemonResponse
from app.services.pokemon_service import PokemonService, PokemonNotFound


router = APIRouter(
    prefix='/pokemons',
    dependencies=[Depends(verify_api_key)]
)

service = PokemonService()

@router.get(
        '/',
        response_model=PokemonListResponse
    )
async def get_pokemons(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    return await service.get_pokemons(
        limit=limit, 
        offset=offset
    )

@router.get(
        '/{name}',
        response_model=PokemonResponse
    )
async def get_pokemon(name: str):
    return await service.get_pokemon(name)
       
