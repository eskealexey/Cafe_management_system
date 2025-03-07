from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Item
from .forms import ItemsForm


def list_menu(request):
    """
    Список блюд
    """
    menu = Item.objects.filter(delete_is=False).order_by('name')
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Блюдо успешно добавлено.')
            return redirect('list_menu')
    else:
        form = ItemsForm()
    context = {
        'menu': menu,
        'title': 'Список блюд',
        'form': form,
    }
    return render(request, 'menu/list_menu.html', context=context)


def menu_edit_item(request, id):
    """
    Редактирование блюда
    """
    item = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        form = ItemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Блюдо успешно обновлено.')
            return redirect('list_menu')
    else:
        form = ItemsForm(instance=item)
    context = {
        'item': item,
        'form': form,
        'title': 'Редактирование блюда',
    }
    return render(request, 'menu/edit_item.html', context=context)


def confirm_delete_item(request, id):
    """
    Подтверждение удаления блюда
    """
    item = get_object_or_404(Item, pk=id)
    context = {
        'id': id,
        'item': item,
        'title': 'Подтверждение удаления блюда',
    }
    return render(request, 'menu/confirm_delete_item.html', context=context)


def delete_item(request, id):
    """
    Удаление блюда
    """
    item = get_object_or_404(Item, id=id)
    if not item.delete_is:
        item.delete_is = True
        item.active_is = False
        item.save()
        messages.success(request, 'Блюдо успешно удалено.')
    else:
        messages.warning(request, 'Блюдо уже удалено.')
    return redirect('list_menu')