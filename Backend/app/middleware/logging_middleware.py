import time
import logging
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

logger = logging.getLogger("clinic_backend")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware to track request processing duration and status codes.
    """
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = (time.time() - start_time) * 1000
        
        logger.info(
            f"Method={request.method} Path={request.url.path} "
            f"Status={response.status_code} Duration={process_time:.2f}ms"
        )
        response.headers["X-Process-Time-Ms"] = f"{process_time:.2f}"
        return response
