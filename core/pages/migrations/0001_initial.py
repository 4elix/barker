# Generated by Django 5.0.7 on 2024-08-03 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя категории')),
                ('image', models.ImageField(upload_to='image/categories/', verbose_name='Картинка категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО работника')),
                ('years_experience', models.IntegerField(default=0, verbose_name='Годы опыта')),
                ('image', models.ImageField(upload_to='image/categories/', verbose_name='Фото работника')),
                ('position', models.CharField(choices=[('с', 'стажер'), ('к', 'кондитер'), ('п', 'пекарь'), ('гп', 'главный пекарь')], default='c', max_length=2)),
                ('facebook', models.CharField(max_length=200, verbose_name='Ссылка на facebook')),
                ('twitter', models.CharField(max_length=200, verbose_name='Ссылка на twitter')),
                ('instagram', models.CharField(max_length=200, verbose_name='Ссылка на instagram')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('price', models.IntegerField(default=0, verbose_name='Стоимость')),
                ('description', models.TextField(verbose_name='Описание на детальную страницу')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество')),
                ('slug', models.SlugField(max_length=255, verbose_name='ссылка до продукта')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='pages.products')),
            ],
        ),
    ]
