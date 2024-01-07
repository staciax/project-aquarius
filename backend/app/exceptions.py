from typing import Any

from django.http import HttpRequest
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.exceptions import APIException
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
    response = exception_handler(exc, context)
    if response is None and isinstance(exc, Exception):
        return Response(
            {
                'error': str(exc),
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if response is None:
        return Response(
            {
                'error': 'Server Error.',
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if isinstance(exc, APIException):
        response.data = {
            'error': exc.detail[0] if len(exc.detail) == 1 and isinstance(exc.detail, list) else exc.detail,
            'status_code': exc.status_code,
        }

    # rename 'detail' key to 'error'
    if response is not None and isinstance(response.data, dict) and 'detail' in response.data:
        response.data['error'] = response.data['detail']
        del response.data['detail']
        response.data['status_code'] = response.status_code

    return response
