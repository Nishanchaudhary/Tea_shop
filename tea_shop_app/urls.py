from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('base',base, name='base'),
    path('',index, name='index'),
    path('product_list', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('like/',like_product, name='like_product'),
    path('search/',search_products, name='search'),
    path('about',about, name='about'),
    path('testimonial', testimonial, name='testimonial'),
    path('blog', blog, name='blog'),
    path('<int:pk>/',blog_detail, name='blog_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)