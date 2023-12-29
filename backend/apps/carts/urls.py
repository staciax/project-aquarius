from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.CartList.as_view()),
    path('<int:id>/', views.CartDetail.as_view()),
    path('items/', views.CartItemList.as_view()),
    path('items/<int:id>/', views.CartItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
