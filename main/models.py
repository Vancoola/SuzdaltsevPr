from django.db import models
import stripe
from django.utils.html import format_html


# Create your models here.

class ItemModels(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255, blank=False, null=False)
    description = models.TextField(verbose_name='Описание', blank=False, null=False)
    price = models.IntegerField(verbose_name='Цена', blank=False, null=False)
    item_token = models.CharField(verbose_name='Токен', max_length=1000, blank=True)

    def __str__(self):
        return self.name

    def price_warning(self):
        return format_html('<h1 style="color: red">{}</h1>',
                           'Внимание! Минимальная сумма 5000, т.к. Аккаунт привязан к JPY')

    price_warning.short_description = 'Цены'

    def save(self, **kwargs):
        stripe.api_key = 'sk_test_51OPTgAHzaSo6OINVPmF0zIYQIgpBqcqZxhFdyzQ81NNIjSMxHe3nOCdzx3siBpT2B9aEe84IC5ApSHixMG8Z8DA8009HaKGVkr'
        # print(self.name)
        self.item_token = stripe.Price.create(
            currency="rub",
            unit_amount=self.price,
            product_data={"name": self.name},
        )['id']
        super(ItemModels, self).save()


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['price']
