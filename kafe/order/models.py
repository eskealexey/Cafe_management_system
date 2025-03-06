from django.db import models

from menu.models import Item
#
#
# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('0', 'В ожидании'),
#         ('1', 'Готово'),
#         ('2', 'оплачено'),
#     ]
#     table_number = models.IntegerField(verbose_name='номер стола')
#     items = models.ManyToManyField(Item, verbose_name='Блюда',limit_choices_to={'active_is': True})  # Фильтр для выбора только активных блюд)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость заказа', blank=True, null=True)
#     status = models.CharField(max_length=1, blank=True, choices=STATUS_CHOICES, default='0', verbose_name='статус заказа')
#
#     @property
#     def active_items(self):
#         return self.items.filter(active_is=True)
#
#     def __str__(self):
#         return f"Заказ #{self.id} на столе {self.table_number}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('0', 'В ожидании'),
        ('1', 'Готово'),
        ('2', 'Оплачено'),
    ]
    table_number = models.IntegerField(verbose_name='Номер стола')
    items = models.ManyToManyField(
        Item,
        verbose_name='Блюда',
        limit_choices_to={'active_is': True}  # Фильтр для выбора только активных блюд
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Стоимость заказа',
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=1,
        blank=True,
        choices=STATUS_CHOICES,
        default='0',
        verbose_name='Статус заказа'
    )

    @property
    def active_items(self):
        return self.items.filter(active_is=True)

    def calculate_total_price(self):
        self.total_price = sum(item.price for item in self.items.all())
        self.save()

    def __str__(self):
        return f"Заказ #{self.id if self.id else 'новый'} на столе {self.table_number}"