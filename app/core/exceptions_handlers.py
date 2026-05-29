from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

from app.core.logger import logger
from app.core.exceptions import PokemonNotFound

async def pokemon_not_found_handler(request: Request,exc: PokemonNotFound):
    logger.exception(
        'PokemonNotFound error occurred',
        extra={
            'error': str(exc),
            'path': str(request.url.path)
        }   
    )
    
    return JSONResponse(
        status_code=404,
        content={
            'error': 'PokemonNotFound',
            'detail': str(exc)
        }
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning(
        'HTTPException occurred',
        extra={
            'status_code': exc.status_code,
            'detail': str(exc.detail),
            'path': str(request.url.path)    
        }
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            'error': 'HTTPException',
            'message': exc.detail
        }
    )


