from django.urls import path
from .views import index
from .views import portfolio

app_name = "portfolio"

urlpatterns = [
    path('', index, name='index'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/contact/', portfolio, name='portfolio/contact/'),
    path('portfolio/services/', portfolio, name='portfolio/services/'),
    path('portfolio/about/', portfolio, name='portfolio/about/'),
]