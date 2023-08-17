from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, products, ProductDetailView, ProductListView, BlogListView, BlogCreateView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view()),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('blog_detail/<slug:slug>', BlogDetailView.as_view(), name='blog_view'),
    path('blog_edit/<slug:slug>', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog_delete/<slug:slug>', BlogDeleteView.as_view(), name='blog_delete'),
]
