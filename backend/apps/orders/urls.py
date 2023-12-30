from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# TODO: create order by cart

urlpatterns = [
    path('', views.OrderList.as_view()),
    path('<int:id>/', views.OrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
