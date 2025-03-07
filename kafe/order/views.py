from django.contrib import messages
from django.db import DatabaseError
from django.db.models import Q, Sum
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import OrderForm, OrderStatusForm
from .models import Order


class OrdersView(View):
    """
    Список заказов
    """
    def get(self, request):
        """
        Список заказов
        """
        orders = Order.objects.all().order_by('-id')

        context = {
            'orders': orders,
            'title': 'Список заказов',
        }
        return render(request, 'order/orders.html', context=context)


class OrderAddView(View):
    """
    Добавление заказа
    """
    def get(self, request):
        form = OrderForm()
        context = {
            'title': 'Добавление заказа',
            'form': form,
        }
        return render(request, 'order/order_add.html', context=context)

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                order = Order.objects.last()
                order.calculate_total_price()
                return redirect('view_orders')
            except Exception as e:
                # Логирование ошибки
                print(f"Ошибка при сохранении заказа: {e}")
                return render(request, 'order/error.html', {'message': 'Ошибка при сохранении заказа', 'title': 'Ошибка'})
        else:
            context = {
                'title': 'Добавление заказа',
                'form': form,
            }
            return render(request, 'order/order_add.html', context=context)


class ConfirmDeleteOrderView(View):
    def get(self, request, pk):
        """
        Подтверждение удаления заказа
        """
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            # Обработка случая, когда заказ не найден
            return render(request, 'order/error.html', {'message': 'Заказ не найден', 'title': 'Ошибка'})

        context = {
            'id': pk,
            'order': order,
            'title': 'Подтверждение удаления заказа',
        }
        return render(request, 'order/confirm_delete.html', context=context)


class DeleteOrderView(View):
    def post(self, request, pk):
        """
        Удаление заказа
        """
        try:
            order = Order.objects.get(pk=pk)
            order.delete()
        except Order.DoesNotExist:
            # Обработка случая, когда заказ не найден
            return render(request, 'order/error.html', {'message': 'Заказ не найден', 'title': 'Ошибка'})

        return redirect('view_orders')


class SearchOrdersView(View):
    def get(self, request):
        """
        Поиск заказов по номеру заказа или статусу
        """
        query = request.GET.get('q')
        if query == 'o':
            query = 'о'
        elif query == 'd':
            query = 'в'
        elif query == 'u':
            query = 'г'
        if query:
            try:
                orders = Order.objects.filter(Q(id__icontains=query) | Q(status__icontains=query.lower()))
            except Exception as e:
                # Логирование ошибки
                print(f"Ошибка при поиске заказов: {e}")
                # orders = Order.objects.all()
                return render(request, 'order/error.html', {'message': 'Заказ не найден', 'title': 'Ошибка'})
        else:
            orders = Order.objects.all()

        context = {
            'orders': orders,
        }
        return render(request, 'order/orders.html', context=context)


class ChangeStatusView(View):
    def get(self, request, pk):
        """
        Изменение статуса заказа
        """
        try:
            order = Order.objects.get(id=pk)
        except Order.DoesNotExist:
            return render(request, 'order/error.html', {'message': 'Заказ не найден', 'title': 'Ошибка'})

        form = OrderStatusForm(instance=order)
        context = {
            'order': order,
            'form': form,
            'title': 'Изменение статуса заказа',
        }
        return render(request, 'order/change_status.html', context=context)

    def post(self, request, pk):
        try:
            order = Order.objects.get(id=pk)
        except Order.DoesNotExist:
            return render(request, 'order/error.html', {'message': 'Заказ не найден', 'title': 'Ошибка'})

        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            try:
                form.save()
                return redirect('view_orders')
            except Exception as e:
                # Логирование ошибки
                print(f"Ошибка при изменении статуса заказа: {e}")
                return render(request, 'order/error.html', {'message': 'Ошибка при изменении статуса заказа', 'title': 'Ошибка'})


class RevenueForShiftView(TemplateView):
    template_name = 'order/revenue_for_shift.html'

    def get_context_data(self, **kwargs):
        """
        Выручка за смену
        """
        try:
            revenue = Order.objects.filter(status='о').aggregate(total_revenue=Sum('total_price'))['total_revenue']
            if revenue is None:
                revenue = 0  # Если заказов нет, выручка равна 0
        except Exception as e:
            # Логирование ошибки
            print(f"Ошибка при расчете выручки: {e}")
            revenue = 0

        context = {
            'revenue': revenue,
            'title': 'Выручка за смену',
        }
        return context


def clean_order(request):
    """
    Очистка заказов за смену
    """
    if request.method == 'GET':
        try:
            # Очищаем заказы за смену
            Order.objects.all().delete()
            messages.success(request, 'Заказы успешно очищены.')
        except DatabaseError as e:
            messages.error(request, f'Ошибка при очистке заказов: {e}')
    return redirect('view_orders')
