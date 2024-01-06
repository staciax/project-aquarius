from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/<int:order_id>/approve/', views.approve_order),
    path('orders/<int:order_id>/ship/', views.ship_order),
    path('orders/<int:order_id>/cancel/', views.cancel_order),
    path('orders/<int:order_id>/complete/', views.complete_order),
    path('orders/<int:id>/items/', views.OrderItemListCreateView.as_view()),
    path('orders/<int:order_id>/items/<int:item_id>/', views.OrderItemDetail.as_view()),
]
