# Generated by Django 5.0 on 2023-12-28 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):  # type: ignore
    initial = True

    dependencies: list[tuple[str, ...]] = [
        ('genres', '0001_initial'),
        ('product_genres', '0001_initial'),
        ('product_tags', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('isbn', models.CharField(max_length=13)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'genres',
                    models.ManyToManyField(
                        related_name='products', through='product_genres.ProductGenre', to='genres.genre'
                    ),
                ),
                ('tags', models.ManyToManyField(related_name='products', through='product_tags.ProductTag', to='tags.tag')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
