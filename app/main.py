from fastapi import FastAPI

from app.core.database import Base, engine
from app.core.exceptions import pokemon_not_found_handler
from app.core.logging_middleware import LoggingMiddleWare

from app.routes.pokemon_router import router 

from app.services.pokemon_service import PokemonNotFound 


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Pokemon API',
    version='1.0.0'
)

app.add_middleware(LoggingMiddleWare)

app.include_router(router)

app.add_exception_handler(
    PokemonNotFound,
    pokemon_not_found_handler
)

@app.get('/')
def home():
    return {'status': 'Pokemon API'}
