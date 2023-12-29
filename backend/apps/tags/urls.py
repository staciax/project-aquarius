from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.TagList.as_view()),
    path('<int:id>/', views.TagDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
