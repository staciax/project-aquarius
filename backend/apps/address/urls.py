from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns: list[path] = [
    path('', views.AddressList.as_view()),
    path('<int:id>/', views.AddressDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
