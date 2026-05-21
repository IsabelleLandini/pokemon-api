from fastapi import APIRouter, HTTPException
from app.services.pokemon_service import PokemonService

router = APIRouter(prefix='/pokemon', tags=['Pokemon'])

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
