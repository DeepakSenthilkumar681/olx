from django.urls import path
from . import views

app_name = 'olx'

urlpatterns = [
    path('', views.index, name='index'), 
    path('<str:id>/',views.detail, name='detail'),
]
