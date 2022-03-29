from django.contrib import admin
from django.urls import path
from . import views

app_name = 'test1219'
urlpatterns = [
    path('', views.index, name='index'),  # /polls/
    path('maps/', views.maps, name='maps')
]
