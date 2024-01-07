from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('', include('api.user.urls')),
    path('', include('api.address.urls')),
    path('', include('api.cart.urls')),
    path('', include('api.customers.urls')),
    path('', include('api.genres.urls')),
    path('', include('api.orders.urls')),
    path('', include('api.payments.urls')),
    path('', include('api.product_tagging.urls')),
    path('', include('api.products.urls')),
    path('', include('api.tags.urls')),
]
