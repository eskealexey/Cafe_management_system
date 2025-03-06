from django.db.models import Q, Sum
from django.shortcuts import render, redirect

from order.forms import OrderForm, OrderStatusForm
from order.models import Order


def orders_view (request):
    """
    Список заказов
    """
    orders = Order.objects.all().order_by('-id')

    context = {
        'orders': orders,
        'title': 'Список заказов',
    }
    return render(request, 'order/orders.html', context=context)


def order_add(request):
    """
    Добавление заказа
    """
    if request.method == 'POST':
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
        form = OrderForm()

    context = {
        'title': 'Добавление заказа',
        'form': form,
    }
    return render(request, 'order/order_add.html', context=context)


def confirm_delete_order(request, id):
    """
    Подтверждение удаления заказа
    """
    try:
        order = Order.objects.get(pk=id)
    except Order.DoesNotExist:
        # Обработка случая, когда заказ не найден
        return render(request, 'order/error.html', {'message': 'Заказ не найден', 'title': 'Ошибка'})

    if request.method == 'GET':
        context = {
            'id': id,
            'order': order,
            'title': 'Подтверждение удаления заказа',
        }
        return render(request, 'order/confirm_delete.html', context=context)


def delete_order(request, id):
    """
    Удаление заказа
    """
    try:
        order = Order.objects.get(pk=id)
        order.delete()
    except Order.DoesNotExist:
        # Обработка случая, когда заказ не найден
        return render(request, 'order/error.html', {'message': 'Заказ не найден', 'title': 'Ошибка'})

    return redirect('view_orders')


def search_orders(request):
    """
    Поиск заказов по номеру заказа или статусу
    """
    query = request.GET.get('q')
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


def change_status(request, id):
    """
    Изменение статуса заказа
    """
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return render(request, 'order/error.html', {'message': 'Заказ не найден', 'title': 'Ошибка'})

    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            try:
                form.save()
                return redirect('view_orders')
            except Exception as e:
                # Логирование ошибки
                print(f"Ошибка при изменении статуса заказа: {e}")
                return render(request, 'order/error.html', {'message': 'Ошибка при изменении статуса заказа', 'title': 'Ошибка'})
    else:
        form = OrderStatusForm(instance=order)
        context = {
            'order': order,
            'form': form,
            'title': 'Изменение статуса заказа',
        }
        return render(request, 'order/change_status.html', context=context)


def revenue_for_shift(request):
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
    return render(request, 'order/revenue_for_shift.html', context=context)
