from django.contrib import admin
from django.urls import path
from .views import product_list, product_detail, obtain_token


app_name = "api"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name="product_list"),
    path('products/<int:id>/', product_detail, name='product-detail'),
    path('token/', obtain_token, name='obtain-token'),
]
