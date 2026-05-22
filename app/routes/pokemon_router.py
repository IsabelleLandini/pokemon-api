from fastapi import APIRouter, HTTPException
from app.services.pokemon_service import PokemonService

router = APIRouter(prefix='/pokemons', tags=['Pokemon'])

service = PokemonService()

@router.get('/{name}')
async def get_pokemon(name:str):
    pokemon = await service.get_pokemon(name)

    if not pokemon:
        raise HTTPException(
              status_code=404,
              detail='Pokémon não encontrado'  
        )
    
    return pokemon

@router.get('')
async def get_pokemons(
    limit: int = 20,
    offset: int = 0    
):
    return await service.get_pokemons(
        limit=limit,
        offset=offset
    )