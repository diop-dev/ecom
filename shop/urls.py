from django.urls import path
from shop.views import index, detail, checkout, confimation
from .import views 







urlpatterns = [
    path('',index, name='home'),
  
    
    path('product/<str:item_name>/', views.detail, name='detail'),
    path('<int:myid>', detail, name="detail"),
    path("checkout", checkout, name="checkout"),
    path('confirmation', confimation, name="confirmation"),
   
]




