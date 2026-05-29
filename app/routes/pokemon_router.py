from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import verify_api_key

from app.models.pokemon import Pokemon

from app.schemas.pokemon_schema import PokemonListResponse, PokemonResponse, PokemonCreate

from app.services.pokemon_service import PokemonService


router = APIRouter(
    prefix='/pokemons',
    dependencies=[Depends(verify_api_key)]
)

service = PokemonService()

@router.post('/')
def create_pokemon(
    pokemon: PokemonCreate,
    db: Session = Depends(get_db)    
):
    db_pokemon = Pokemon(
        pokemon_id=pokemon.pokemon_id,
        name=pokemon.name,
        height=pokemon.weight,
        types=pokemon.types,
        front_sprite=pokemon.front_sprite,
        back_sprite=pokemon.back_sprite
    )

    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)

    return db_pokemon

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
       
