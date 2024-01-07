import time
from typing import Callable

from django.http import HttpRequest, HttpResponse


class AppMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start
        response['X-Process-Time'] = str(duration)
        return response
