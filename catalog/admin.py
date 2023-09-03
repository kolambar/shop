from django.contrib import admin

from catalog.models import Category, Product, Blog, Version


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'cost', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'header', 'slug', 'creation_date',)
    list_filter = ('header', 'creation_date')
    search_fields = ('name', 'text',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'is_current_version',)
    list_filter = ('is_current_version', 'product')
    search_fields = ('product', 'version_name',)
