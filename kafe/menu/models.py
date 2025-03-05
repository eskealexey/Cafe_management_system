from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    active_is = models.BooleanField(default=True)
    delete_is = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.price} руб'