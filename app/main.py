from fastapi import FastAPI

from app.core.database import Base, engine
from app.routes.pokemon_router import router as pokemon_router 

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Pokemon API',
    version='1.0.0'
)

app.include_router(pokemon_router)

@app.get('/')
def home():
    return {'status': 'Pokemon API'}
