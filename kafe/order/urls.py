from django.urls import path
from django.contrib.auth import views as auth_views
from .views import orders_view, order_add, confirm_delete_order, delete_order, search_orders, change_status, revenue_for_shift


urlpatterns = [
    path('view/', orders_view, name='view_orders'),
    path('add/', order_add, name='order_add'),
    path('confdelete/<int:id>/', confirm_delete_order, name='confirm_delete_order'),
    path('delete/<int:id>/', delete_order, name='delete_order'),
    path('search/', search_orders, name='search_orders'),
    path('change/<int:id>/', change_status, name='change_status'),
    path('revenue/', revenue_for_shift, name='revenue_for_shift'),
]