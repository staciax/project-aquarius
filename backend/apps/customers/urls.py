from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.CustomerList.as_view()),
    path('<int:id>/', views.CustomerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
