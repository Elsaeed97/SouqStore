from django.urls import path
from . import views
urlpatterns = [
     path('', views.product_list, name='product_list'),
     path('checkout/',views.checkout, name='chechout'),
     path('<slug:slug>/', views.product_detail, name='product_detail'),

     
]