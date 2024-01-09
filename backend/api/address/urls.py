from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'address', views.AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('address/@me', views.AddressMeView.as_view()),
]
