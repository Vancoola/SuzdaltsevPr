# Generated by Django 5.0 on 2023-12-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmodels',
            name='item_token',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Токен'),
        ),
        migrations.AlterField(
            model_name='itemmodels',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]