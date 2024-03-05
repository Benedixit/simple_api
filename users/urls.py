from django.contrib import admin
from django.urls import path
from .views import create_user, login_user

app_name = "users"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', create_user, name="Create User"),
    path('api/login/', login_user, name="User Login")
]
