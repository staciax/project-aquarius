from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('users/', views.UserList.as_view()),
    # path('users/login/', views.user_login),
    # path('users/register/', views.user_register),
    # path('users/logout/', views.user_logout),
    # path('users/forgot-password/', views.user_forgot_password),
]
