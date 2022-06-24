from django.urls import path
from . import views

urlpatterns=[
    path('', views.home),
    path('index.html', views.home),
]