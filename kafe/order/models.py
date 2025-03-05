from django.db import models

from menu.models import Item


# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('0', 'В ожидании'),
#         ('1', 'Готово'),
#         ('2', 'оплачено'),
#     ]
#     table_number = models.IntegerField(verbose_name='номер стола')
#     # items = models.ManyToManyField(Item.objects.filter(active_is=True, delete_is=False), verbose_name='Блюда')
#     items = models.ManyToManyField(Item.objects.filter(active_is=True), verbose_name='Блюда')
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость заказа', blank=True, null=True)
#     status = models.CharField(max_length=1, blank=True, choices=STATUS_CHOICES, default='0', verbose_name='статус заказа')
#
#     def __str__(self):
#         return f"Заказ #{self.id} на столе {self.table_number}"
#

class Order(models.Model):
    STATUS_CHOICES = [
        ('0', 'В ожидании'),
        ('1', 'Готово'),
        ('2', 'оплачено'),
    ]
    table_number = models.IntegerField(verbose_name='номер стола')
    items = models.ManyToManyField(Item, verbose_name='Блюда')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость заказа', blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, choices=STATUS_CHOICES, default='0', verbose_name='статус заказа')

    @property
    def active_items(self):
        return self.items.filter(active_is=True)

    def __str__(self):
        return f"Заказ #{self.id} на столе {self.table_number}"


