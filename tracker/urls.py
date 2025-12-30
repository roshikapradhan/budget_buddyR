from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # This loads your main pink page
]