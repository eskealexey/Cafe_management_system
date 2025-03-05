from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Item
from .forms import ItemsForm


def list_menu(request):
    """
    Список блюд
    """
    menu = Item.objects.filter(delete_is=False).select_related().order_by('name')
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            Item.objects.create(name=form.cleaned_data['name'],
                                price=form.cleaned_data['price'],
                                active_is=form.cleaned_data['active_is'])
            form = ItemsForm()  # Создаем новую форму после успешной отправки
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
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        form = ItemsForm(request.POST, instance=item)
        if form.is_valid():
            item.name = form.cleaned_data['name']
            item.price = form.cleaned_data['price']
            item.active_is = form.cleaned_data['active_is']
            item.save()
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
    item = Item.objects.get(pk=id)
    if request.method == 'GET':

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
    item.delete_is = True
    item.active_is = False
    item.save()
    return redirect('list_menu')
