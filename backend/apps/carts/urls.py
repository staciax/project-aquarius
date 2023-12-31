from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.CartList.as_view()),
    path('<int:id>/', views.CartDetail.as_view()),
    path('<int:cart>/items/', views.CartItemCreateDetail.as_view()),
    path('<int:cart>/items/<int:product>', views.CartItemUpdateDelete.as_view()),
    path('customer/<int:customer_id>/', views.CartDetailByCustomer.as_view()),
    # path('<int:cart_id>/items/<int:product_id>', views.CartDetail.as_view()),
    # path('items/', views.CartItemList.as_view()),
    # path('items/<int:id>/', views.CartItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
