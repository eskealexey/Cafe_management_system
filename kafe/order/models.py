from django.db import models

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ('0', 'В ожидании'),
        ('1', 'Готово'),
        ('2', 'оплачено'),
    ]
    table_number = models.IntegerField(verbose_name='номер стола')
    items = models.ManyToManyField('Item', verbose_name='Название')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total price', blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, choices=STATUS_CHOICES, default='0', verbose_name='вкус ягоды')

    def __str__(self):
        return f"Заказ #{self.id} на столе {self.table_number}"


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name