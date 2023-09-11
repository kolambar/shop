from django.core.cache import cache

from config import settings


def get_products_of_(queryset, pk):
    '''
    Получает товары категории с заданной pk, а также, если включено кэширование, кэширует список товаров
    '''
    if settings.CACHE_ENABLED:
        key = 'product_list' + str(pk)
        product_list = cache.get(key)
        if product_list is None:
            product_list = queryset.filter(category=pk)
            cache.set(key, product_list)
    else:
        product_list = queryset.filter(category=pk)

    return product_list
