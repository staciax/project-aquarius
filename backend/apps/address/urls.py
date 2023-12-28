from django.urls import path

from . import views

urlpatterns: list[path] = [
    path('', views.root, name='root'),
    path('address/', views.get_address, name='get_address'),
]
