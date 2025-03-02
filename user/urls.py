from django.urls import path
from .views import add_user, all, delete_user, get_user, update_user

app_name = "user"


urlpatterns = [
    path('', all, name='all'),
    path('<str:id>', get_user, name='get_user'),
    path('add/', add_user, name='get_user'),
    path('update/<str:id>', update_user, name='get_user'),
    path('delete/<str:id>', delete_user, name='get_user'),
]
