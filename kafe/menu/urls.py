from django.urls import path

from .views import list_menu, menu_edit_item

urlpatterns = [
    path('menu/', list_menu, name='list_menu'),
    path('edit/<int:id>/', menu_edit_item, name='menu_edit_item'),
]