# Generated by Django 5.0 on 2023-12-30 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('street_address', models.CharField(max_length=512)),
                ('province', models.CharField(max_length=128)),
                ('district', models.CharField(max_length=128)),
                ('postal_code', models.CharField(max_length=5)),
                ('phone_number', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'customer',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, related_name='address2', to='customers.customer'
                    ),
                ),
            ],
        ),
    ]
