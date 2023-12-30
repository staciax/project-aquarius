from typing import Any

from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc: Exception, context: dict[str, Any]) -> Response:
    response = exception_handler(exc, (IntegrityError))
    if response is None and isinstance(exc, Exception):
        return Response(
            {
                'detail': str(exc),
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    response.data['status_code'] = response.status_code
    return response
