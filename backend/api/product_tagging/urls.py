from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'product_tagging', views.ProductTagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
