from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from app.models.pokemon import Pokemon

class PokemonDBService:
    @staticmethod
    def create(db: Session, data):
        try:
            pokemon = Pokemon(**data)
            db.add(pokemon)
            db.commit()
            db.refresh(pokemon)
            return pokemon
        
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=409,
                detail='Pokemon alredy exists'
            )
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
        try:
            for key, value in data.items():
                setattr(pokemon, key, value)
            db.commit()
            db.refresh(pokemon)
            return pokemon
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=409,
                detail='Error updating pokemon'
            )

    @staticmethod
    def delete(db: Session, pokemon):
        try:
            db.delete(pokemon)
            db.commit()
        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=500,
                detail='Error deleting pokemon'
            )
