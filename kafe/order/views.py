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


def get_total_price(items):
    total_price = 0
    for item in items:
        total_price += item.price
    return total_price


def order_add(request):
    """
    Добавление заказа
    """
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            table_number = form.cleaned_data.get('table_number')
            items = form.cleaned_data.get('items')
            total_price = get_total_price(items)
            form.save()
            order = Order.objects.last()
            order.total_price = total_price
            order.save()
            return redirect('view_orders')
    else:
        form = OrderForm()

    context = {
        'title': 'Добавление заказа',
        'form': form,
    }
    return render(request, 'order/order_add.html', context=context)

