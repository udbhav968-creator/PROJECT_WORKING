import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger("clinic_core")


def custom_exception_handler(exc, context):
    """
    Industry Standard Custom DRF Exception Handler.
    Flattens error responses into predictable JSON:
    {
        "success": false,
        "errors": ["Error detail 1", "Error detail 2"]
    }
    """
    response = exception_handler(exc, context)

    if response is not None:
        custom_errors = []
        if isinstance(response.data, dict):
            for field, value in response.data.items():
                if isinstance(value, list):
                    for msg in value:
                        custom_errors.append(f"{field}: {msg}" if field != 'detail' else str(msg))
                else:
                    custom_errors.append(f"{field}: {value}" if field != 'detail' else str(value))
        elif isinstance(response.data, list):
            custom_errors = [str(item) for item in response.data]
        else:
            custom_errors = [str(response.data)]

        response.data = {
            "success": False,
            "errors": custom_errors
        }
    else:
        logger.error(f"Unhandled Exception in DRF: {str(exc)}", exc_info=True)
        return Response(
            {
                "success": False,
                "errors": ["An unexpected server error occurred."]
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response
