"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('apps.address/', include('apps.address.urls')),
    path('apps.carts/', include('apps.carts.urls')),
    path('apps.customers/', include('apps.customers.urls')),
    path('apps.genres/', include('apps.genres.urls')),
    path('apps.orders/', include('apps.orders.urls')),
    path('apps.payments/', include('apps.payments.urls')),
    # path('apps.product_genres/', include('apps.product_genres.urls')),
    # path('apps.product_tags/', include('apps.product_tags.urls')),
    path('apps.products/', include('apps.products.urls')),
    path('apps.tags/', include('apps.tags.urls')),
]
