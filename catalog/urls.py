from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductDetailView, ProductListView, BlogListView, BlogCreateView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, ProdOfCatListView

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('products_create/', ProductCreateView.as_view(), name='products_create'),
    path('<int:pk>/update_product/', ProductUpdateView.as_view(), name='update_product'),
    path('products_of_/<int:pk>/', ProdOfCatListView.as_view(), name='products_of_'),

    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('blog_detail/<slug:slug>', BlogDetailView.as_view(), name='blog_view'),
    path('blog_edit/<slug:slug>', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog_delete/<slug:slug>', BlogDeleteView.as_view(), name='blog_delete'),
]
