from django.urls import path
from . import views # from current folder immport views

# /products
# /products/1/details
urlpatterns = [
    path('', views.index),
    path('new/', views.new), # important to have a slash after route name as it will return an error if you dont
]