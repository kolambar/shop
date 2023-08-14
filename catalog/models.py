from django.db import models

# Create your models here.


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    photo = models.ImageField(upload_to='catalog/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Название категории')
    cost = models.IntegerField(verbose_name='Цена')
    creation_date = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    last_change_date = models.DateField(verbose_name='Дата последнего изменения', auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.category} - {self.cost}'

    def __repr__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
