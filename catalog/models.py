from django.db import models

from users.models import User

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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name}, {self.category} - {self.cost}'

    def __repr__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Blog(models.Model):
    header = models.CharField(max_length=100, verbose_name='Заголовок', unique=True)
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    text = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='catalog/', verbose_name='Изображение', **NULLABLE)
    creation_date = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_number = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.header}, {self.creation_date}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Version(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    version_number = models.CharField(max_length=30, verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    is_current_version = models.BooleanField(verbose_name='Текущая версия')

    def __str__(self):
        return f'{self.product}, {self.version_number}, {self.version_name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'