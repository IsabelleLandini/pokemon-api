import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger import logger

class LoggingMiddleWare(BaseHTTPMiddleware):
    async def dispatch(
            self, 
            request, 
            call_next
    ):
        start_time = time.time()

        logger.info(
           f'Request: {request.method} {request.url.path}' 
        )

        response = await call_next(request)

        process_time = time.time() - start_time

        logger.info(
            f'Response: {response.status_code} '
            f' - {process_time:4f}s'  
        )

        return response
    