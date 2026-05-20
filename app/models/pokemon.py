from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Pokemon(Base):
    __tablename__ = 'pokemons'

    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, unique=True, nullable=False)

    name = Column(String, nullable=False)
    height = Column(Integer)
    weight = Column(Integer)

    types = Column(String)

    front_sprite = Column(String)
    back_sprite = Column(String)
    