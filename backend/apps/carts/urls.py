from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns: list[path] = [
    path('', views.CartList.as_view()),
    path('<int:id>/', views.CartDetail.as_view()),
]

urlpatterns = urlpatterns
