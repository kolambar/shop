from django.core.management import BaseCommand

from catalog.models import Product, Category


cat = Category(name='Рассылки')


class Command(BaseCommand):

    Category.objects.all().delete()
    Product.objects.all().delete()

    def handle(self, *args, **options):
        products_list = [
            {
            "name": "Удобный сервис рассылок",
            "description": "- Неограниченная лицензия\n- Поддержка\n- Установка на сервер\n- Получение обновлений",
            "photo": None,
            "category": cat,
            "cost": 140,
            "creation_date": "2023-08-09",
            "last_change_date": None
            }
        ]
        cat.save()

        products_to_create = []
        for product in products_list:
            products_to_create.append(
                Product(**product)
            )

        Product.objects.bulk_create(products_to_create)
