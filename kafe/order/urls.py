from django.urls import path
from django.contrib.auth import views as auth_views
from .views import orders_view, order_add


urlpatterns = [
    path('view/', orders_view, name='view_orders'),
    path('add/', order_add, name='order_add'),
]