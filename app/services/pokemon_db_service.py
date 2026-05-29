from sqlalchemy.orm import Session
from app.models.pokemon import Pokemon

class PokemonDBService:
    @staticmethod
    def create(db: Session, data):
        pokemon = Pokemon(**data)
        db.add(pokemon)
        db.commit()
        db.refresh(pokemon)
        return pokemon
    
    @staticmethod
    def get_all(db: Session):
        return db.query(Pokemon).all()
    
    @staticmethod
    def get_by_id(db: Session, pokemon_id: int):
        return db.query(Pokemon).filter(
            Pokemon.pokemon_id == pokemon_id
        ).first()
    
    @staticmethod
    def update(db: Session, pokemon: Pokemon, data: dict):
        for key, value in data.items():
            setattr(pokemon, key, value)
        db.commit()
        db.refresh(pokemon)
        return pokemon

    @staticmethod
    def delete(db: Session, pokemon):
        db.delete(pokemon)
        db.commit()
