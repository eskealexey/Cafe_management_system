from django.urls import path
from django.contrib.auth import views as auth_views


from .views import *
urlpatterns = [
    path('view/', OrdersView.as_view(), name='view_orders'),
    path('add/', OrderAddView.as_view(), name='order_add'),
    path('confdelete/<int:pk>/', ConfirmDeleteOrderView.as_view(), name='confirm_delete_order'),
    path('delete/<int:pk>/', DeleteOrderView.as_view(), name='delete_order'),
    path('search/', SearchOrdersView.as_view(), name='search_orders'),
    path('change/<int:pk>/', ChangeStatusView.as_view(), name='change_status'),
    path('revenue/', RevenueForShiftView.as_view(), name='revenue_for_shift'),
    path('clean/', clean_order, name='clean_order')
    ]