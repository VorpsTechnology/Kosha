# Generated by Django 3.0.5 on 2023-06-05 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_cart_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
