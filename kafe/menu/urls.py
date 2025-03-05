from django.urls import path

from .views import list_menu, menu_edit_item, confirm_delete_item, delete_item

urlpatterns = [
    path('', list_menu, name='list_menu'),
    path('edit/<int:id>/', menu_edit_item, name='menu_edit_item'),
    path('confdel/<int:id>/', confirm_delete_item, name='confirm_delete_item'),
    path('delete/<int:id>/', delete_item, name='delete_item'),
]