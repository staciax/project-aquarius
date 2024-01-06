from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'cart', views.CartViewSet)
# router.register(r'cart-item', views.CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cart/<int:cart_id>/items/', views.CartItemListCreateView.as_view()),
    path('cart/<int:cart>/items/<int:product>/', views.CartItemDetail.as_view()),
]
