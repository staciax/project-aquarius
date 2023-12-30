from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:id>/', views.ProductDetail.as_view()),
    path('<int:product>/images/', views.ProductImageList.as_view()),
    path('<int:product>/images/<int:id>/', views.ProductImageDetail.as_view()),
    path('inventory/', views.ProductInventoryList.as_view()),
    path('inventory/<int:id>/', views.ProductInventoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
