from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import verify_api_key

from app.schemas.pokemon_schema import PokemonListResponse, PokemonResponse, PokemonCreate

from app.services.pokemon_service import PokemonService
from app.services.pokemon_db_service import PokemonDBService


router = APIRouter(
    prefix='/pokemons',
    dependencies=[Depends(verify_api_key)]
)

service = PokemonService()

# Create
@router.post('/')
def create_pokemon(
    pokemon: PokemonCreate,
    db: Session = Depends(get_db)    
):
    data = pokemon.model_dump()

    return PokemonDBService.create(db, data)

# Read (DB)
@router.get('/db')
def get_saved_pokemons(
    db: Session = Depends(get_db)
):
    return PokemonDBService.get_all(db)

# Read (API externa)
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
       
# Update
@router.put('/{pokemon_id}')
def update_pokemon(
    pokemon_id: int,
    pokemon_data: PokemonCreate,
    db: Session = Depends(get_db)
):
    pokemon = PokemonDBService.get_by_id(db, pokemon_id)

    if not pokemon:
        raise HTTPException(
            status_code=404,
            detail="Pokemon not found"
        )

    return PokemonDBService.update(
        db, 
        pokemon, 
        pokemon_data.model_dump()
    )

# Delete
@router.delete('/{pokemon_id}')
def delete_pokemon(
    pokemon_id: int,
    db: Session = Depends(get_db)
):
    pokemon = PokemonDBService.get_by_id(db, pokemon_id)

    if not pokemon:
        raise HTTPException(
            status_code=404,
            detail="Pokemon not found"
        )
    
    PokemonDBService.delete(db, pokemon)

    return {"message": "Pokemon deleted successfully"}


