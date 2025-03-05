from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, orders_view

urlpatterns = [
    path('', index, name='index'),
    path('view/', orders_view, name='view_orders'),
]