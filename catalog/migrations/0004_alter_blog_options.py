# Generated by Django 4.2.4 on 2023-08-17 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_blog_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
