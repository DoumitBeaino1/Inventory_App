from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name = 'addProduct'),
    path('', views.list, name = 'listAll'),
    path('sort', views.list_Sort, name = 'sort'),
]

