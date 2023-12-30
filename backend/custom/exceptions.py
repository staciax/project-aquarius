from typing import Any

from django.http import HttpRequest
from django.http.response import JsonResponse


def bad_request(request: HttpRequest, exception: Exception, *args: Any, **kwargs: Any) -> JsonResponse:
    return JsonResponse({'error': 'Bad Request (400)'}, status=400)


def forbidden(request: HttpRequest, exception: Exception, *args: Any, **kwargs: Any) -> JsonResponse:
    return JsonResponse({'error': 'Forbidden (403)'}, status=403)


def not_found(request: HttpRequest, exception: Exception, *args: Any, **kwargs: Any) -> JsonResponse:
    return JsonResponse({'error': 'Not Found (404)'}, status=404)


def server_error(request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse:
    return JsonResponse({'error': 'Server Error (500)'}, status=500)
