# Generated by Django 3.2.6 on 2021-08-30 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_invoice_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoice_no',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
