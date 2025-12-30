from django.urls import path
from tracker import views

urlpatterns = [
    path('', views.index, name='index'),
    path('split/', views.bill_split, name='bill_split'), # Example
    path('notifications/', views.notifications, name='notifications'), # Example
]