from typing import Any

from django.db.utils import IntegrityError
from django.http import HttpRequest
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def bad_request(request: HttpRequest, exception: Exception, *args: Any, **kwargs: Any) -> JsonResponse:
    return JsonResponse({'error': 'Bad Request.', 'status_code': 400}, status=400)


def forbidden(request: HttpRequest, exception: Exception, *args: Any, **kwargs: Any) -> JsonResponse:
    return JsonResponse({'error': 'Forbidden.', 'status_code': 403}, status=403)


def not_found(request: HttpRequest, exception: Exception, *args: Any, **kwargs: Any) -> JsonResponse:
    return JsonResponse({'error': 'Not Found.', 'status_code': 404}, status=404)


def server_error(request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse:
    return JsonResponse({'error': 'Server Error.', 'status_code': 500}, status=500)


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

    # rename 'detail' key to 'error'
    if 'detail' in response.data:
        response.data['error'] = response.data['detail']
        del response.data['detail']
    response.data['status_code'] = response.status_code

    return response
