from pydantic import BaseModel

class PokemonSprites(BaseModel):
    front_default: str | None
    back_default: str | None

class PokemonResponse(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    types: list[str]
    sprites: PokemonSprites
    stats: dict[str, int] | None = None

class PaginationResponse(BaseModel):
    total: int 
    limit: int
    offset: int
    next: str | None
    previous: str |  None

class PokemonListResponse(BaseModel):
    data: list[PokemonResponse]
    pagination: PaginationResponse
