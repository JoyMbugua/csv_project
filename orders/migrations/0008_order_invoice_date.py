# Generated by Django 3.2.6 on 2021-08-30 08:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_remove_order_invoice_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoice_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
