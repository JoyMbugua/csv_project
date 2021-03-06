# Generated by Django 3.2.6 on 2021-08-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='csvs')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('entered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(blank=True, max_length=6, null=True)),
                ('stock_code', models.CharField(blank=True, max_length=6, null=True)),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('invoice_date', models.DateTimeField(auto_now_add=True)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('customerID', models.PositiveIntegerField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
