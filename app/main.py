from fastapi import FastAPI

from app.core.database import Base, engine
from app.models.pokemon import Pokemon

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def home():
    return {'status': 'Pokemon API'}
