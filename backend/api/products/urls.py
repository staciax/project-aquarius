from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:product>/images/', views.ProductImageList.as_view()),
    path('products/<int:product>/images/<int:id>/', views.ProductImageDetail.as_view()),
]
