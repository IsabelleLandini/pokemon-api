from fastapi import FastAPI, HTTPException

from app.core.database import Base, engine
from app.core.exceptions import PokemonNotFound
from app.core.exceptions_handlers import pokemon_not_found_handler, http_exception_handler
from app.core.logging_middleware import LoggingMiddleWare

from app.routes.pokemon_router import router 

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Pokemon API',
    version='1.0.0'
)

app.add_middleware(LoggingMiddleWare)

app.include_router(router)

# Handlers globais
app.add_exception_handler(PokemonNotFound, pokemon_not_found_handler)
app.add_exception_handler(HTTPException,http_exception_handler)

@app.get('/')
def home():
    return {
        'project': 'Pokemon API', 
        'status': 'online',
        'docs': '/docs',
        'demo_api_key': 'pokemon123'
    }
