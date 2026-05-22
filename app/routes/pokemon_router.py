from fastapi import APIRouter, HTTPException, Query
from app.services.pokemon_service import PokemonService, PokemonNotFound

router = APIRouter()

service = PokemonService()

@router.get('/pokemons')
async def get_pokemons(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    return await service.get_pokemons(limit=limit, offset=offset)

@router.get('/pokemons/{name}')
async def get_pokemon(name: str):
    try:
        return await service.get_pokemon(name)
    except PokemonNotFound:
        raise HTTPException(
            status_code=404,
            detail=f"Pokemon '{name}' not found"
        )