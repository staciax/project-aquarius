# Generated by Django 5.0 on 2023-12-31 10:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelTable(
            name='tag',
            table='tags',
        ),
    ]
