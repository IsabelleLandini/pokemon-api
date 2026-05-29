from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import verify_api_key

from app.schemas.pokemon_schema import PokemonListResponse, PokemonResponse, PokemonCreate

from app.services.pokemon_service import PokemonService
from app.services.pokemon_db_service import PokemonDBService


router = APIRouter(
    prefix='/pokemons',
    dependencies=[Depends(verify_api_key)],
    tags=["Pokemons"]
)

service = PokemonService()

# Create
@router.post(
        '/',
        summary='Create Pokemon',
        description='Creates and stores a Pokemon in the database using SQLAlchemy persistence.',
        response_description='Created Pokemon object'
    )
def create_pokemon(
    pokemon: PokemonCreate,
    db: Session = Depends(get_db)    
):
    data = pokemon.model_dump()

    return PokemonDBService.create(db, data)

# Read (DB)
@router.get(
        '/db',
        summary='Get saved Pokemon',
        description='Returns all Pokemon stored in the database.',
        response_description='List of Pokemon from database'
    )
def get_saved_pokemons(
    db: Session = Depends(get_db)
):
    return PokemonDBService.get_all(db)

# Read (API externa)
@router.get(
        '/',
        response_model=PokemonListResponse,
        summary='List Pokemon (external API)',
        description='Fetches Pokemon data from PokeAPI with pagination support.',
        response_description='Paginated list of Pokemon'
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
        response_model=PokemonResponse,
        summary='Get Pokemon by name',
        description='Fetches a specific Pokemon from PokeAPI using its name.',
        response_description='Pokemon details'
)
async def get_pokemon(name: str):
    return await service.get_pokemon(name)
       
# Update
@router.put(
        '/{pokemon_id}',
        summary='Update Pokemon',
        description='Updates an existing Pokemon in the database by its ID.',
        response_description='Updated Pokemon object'
    )
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
@router.delete(
        '/{pokemon_id}',
        summary='Delete Pokemon',
        description='Removes a Pokemon from the database using its ID.',
        response_description='Confirmation message'
)
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


