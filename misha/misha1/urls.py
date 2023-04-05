from django.urls import path

from . import views

urlpatterns = [
    path('index/work/', views.work),
    path('index/contractor/', views.contractor),
    path('index/customer/', views.customer),
    path('index/', views.index),

]