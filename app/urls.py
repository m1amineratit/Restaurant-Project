from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menus, name='menus'),
    path('reservation/', views.reservation, name='reservation')
]