from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('banner-list/', views.list_banner),
    path('banner-create/', views.create_banner),
    # -----------------------------------------
    path('price-list/', views.list_price),
    path('price-create/', views.create_price),
    # -----------------------------------------
    path('about-list/', views.list_about),
    path('about-create/', views.create_about),
    # -----------------------------------------
    path('service-list/', views.list_service),
    path('service-create/', views.create_service),
]