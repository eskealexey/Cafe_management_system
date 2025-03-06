from django.shortcuts import render, redirect

from order.models import Order

from order.forms import OrderForm


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
            form.save()
            order = Order.objects.last()
            order.calculate_total_price()
            return redirect('view_orders')
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
    order = Order.objects.get(pk=id)
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
    order = Order.objects.get(pk=id)
    order.delete()

    return redirect('view_orders')