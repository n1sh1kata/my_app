from django.urls import path
from .views import index
from .views import portfolio
from .views import dashboard

app_name = "portfolio"


urlpatterns = [
    path('', index, name='index'),
    path('dashboard/home/', dashboard, name='dashboard/home/'),
    path('dashboard/report/', dashboard, name='dashboard/report/'),
    path('dashboard/settings/', dashboard, name='dashboard/settings/'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/contact/', portfolio, name='portfolio/contact/'),
    path('portfolio/services/', portfolio, name='portfolio/services/'),
    path('portfolio/about/', portfolio, name='portfolio/about/'),
]