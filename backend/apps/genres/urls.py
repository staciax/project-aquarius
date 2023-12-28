from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns: list[path] = [
    path('', views.GenreList.as_view()),
    path('<int:id>/', views.GenreDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
