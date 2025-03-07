from django.contrib import messages
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import DatabaseError
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, UpdateView, DetailView

from .forms import ItemsForm
from .models import Item


class MenuListView(FormView, ListView):
    """
    Список блюд
    """
    model = Item
    form_class = ItemsForm
    template_name = 'menu/list_menu.html'
    context_object_name = 'menu'
    success_url = reverse_lazy('list_menu')

    def get_queryset(self):
        try:
            # Получаем отфильтрованный и отсортированный список блюд
            return Item.objects.filter(delete_is=False).order_by('name')
        except DatabaseError as e:
            # Логируем ошибку базы данных и возвращаем пустой queryset
            messages.error(self.request, 'Ошибка при загрузке списка блюд. Пожалуйста, попробуйте позже.')
            return Item.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список блюд'
        return context

    def form_valid(self, form):
        try:
            # Сохраняем форму и добавляем сообщение об успехе
            form.save()
            messages.success(self.request, 'Блюдо успешно добавлено.')
        except ValidationError as e:
            # Обрабатываем ошибки валидации
            messages.error(self.request, f'Ошибка при добавлении блюда: {e}')
        except DatabaseError as e:
            # Обрабатываем ошибки базы данных
            messages.error(self.request, 'Ошибка при сохранении блюда. Пожалуйста, попробуйте позже.')
        except Exception as e:
            # Обрабатываем все остальные исключения
            messages.error(self.request, f'Произошла непредвиденная ошибка: {e}')
        return super().form_valid(form)


class MenuEditItemView(UpdateView):
    """
    Редактирование блюда
    """
    model = Item
    form_class = ItemsForm
    template_name = 'menu/edit_item.html'
    context_object_name = 'item'
    success_url = reverse_lazy('list_menu')

    def get_object(self, queryset=None):
        """
        Получаем объект для редактирования. Если объект не найден, возвращаем 404.
        """
        try:
            return super().get_object(queryset)
        except ObjectDoesNotExist:
            messages.error(self.request, 'Блюдо не найдено.')
            return redirect('list_menu')

    def get_context_data(self, **kwargs):
        """
        Добавляем заголовок в контекст.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование блюда'
        return context

    def form_valid(self, form):
        """
        Обрабатываем успешное сохранение формы.
        """
        try:
            form.save()
            messages.success(self.request, 'Блюдо успешно обновлено.')
        except ValidationError as e:
            # Обрабатываем ошибки валидации
            messages.error(self.request, f'Ошибка при обновлении блюда: {e}')
        except DatabaseError as e:
            # Обрабатываем ошибки базы данных
            messages.error(self.request, 'Ошибка при сохранении блюда. Пожалуйста, попробуйте позже.')
        except Exception as e:
            # Обрабатываем все остальные исключения
            messages.error(self.request, f'Произошла непредвиденная ошибка: {e}')
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Обрабатываем случай, если форма не прошла валидацию.
        """
        messages.error(self.request, 'Пожалуйста, исправьте ошибки в форме.')
        return super().form_invalid(form)


class ConfirmDeleteItemView(DetailView):
    """
    Класс для подтверждения удаления блюда
    """
    model = Item
    template_name = 'menu/confirm_delete_item.html'
    context_object_name = 'item'

    def get_object(self, queryset=None):
        """
        Получаем объект для подтверждения удаления. Если объект не найден, возвращаем 404.
        """
        try:
            # Получаем объект по pk из URL
            return super().get_object(queryset)
        except ObjectDoesNotExist:
            messages.error(self.request, 'Блюдо не найдено.')
            return redirect('list_menu')

    def get_context_data(self, **kwargs):
        """
        Добавляем дополнительные данные в контекст.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Подтверждение удаления блюда'
        context['id'] = self.object.pk  # Передаем id объекта в контекст
        return context



def delete_item(request, pk):
    """
    Удаление блюда
    """
    item = get_object_or_404(Item, id=pk)
    if not item.delete_is:
        item.delete_is = True
        item.active_is = False
        item.save()
        messages.success(request, 'Блюдо успешно удалено.')
    else:
        messages.warning(request, 'Блюдо уже удалено.')
    return redirect('list_menu')
