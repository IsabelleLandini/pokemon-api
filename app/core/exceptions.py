from fastapi import Request
from fastapi.responses import JSONResponse

from app.services.pokemon_service import PokemonNotFound

from app.core.logger import logger

async def pokemon_not_found_handler(
    request: Request,
    exc: PokemonNotFound
):
    logger.error(str(exc))
    
    return JSONResponse(
        status_code=404,
        content={
            'detail': str(exc)       
        }
    )
