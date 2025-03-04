from django.shortcuts import render

from order.models import Order


# Create your views here.
def index(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'index_template.html', context=context)


def orders_view (request):
    orders = Order.objects.all()

    context = {
        'orders': orders,
        'title': 'Список заказов',
    }
    return render(request, 'order/orders.html', context=context)