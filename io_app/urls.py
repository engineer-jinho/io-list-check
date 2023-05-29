from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ai/<int:pk>/', views.ai_detail, name='ai_detail'),
    path('ai_hmi/<int:pk>/', views.ai_detail_hmi, name='ai_detail_hmi'),
    
    path('di/<int:pk>/', views.di_detail, name='di_detail'),
    path('do/<int:pk>/', views.do_detail, name='do_detail'),
    path('ao/<int:pk>/', views.ao_detail, name='ao_detail'),
]