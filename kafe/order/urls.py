from django.urls import path
from django.contrib.auth import views as auth_views
from .views import orders_view, order_add, confirm_delete_order, delete_order


urlpatterns = [
    path('view/', orders_view, name='view_orders'),
    path('add/', order_add, name='order_add'),
    path('confdelete/<int:id>/', confirm_delete_order, name='confirm_delete_order'),
    path('delete/<int:id>/', delete_order, name='delete_order'),
]