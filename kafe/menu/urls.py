from django.urls import path

from .views import MenuListView, MenuEditItemView, ConfirmDeleteItemView, delete_item

urlpatterns = [
    path('', MenuListView.as_view(), name='list_menu'),
    path('edit/<int:pk>/', MenuEditItemView.as_view(), name='menu_edit_item'),
    path('confdel/<int:pk>/', ConfirmDeleteItemView.as_view(), name='confirm_delete_item'),
    path('delete/<int:pk>/', delete_item, name='delete_item'),
]