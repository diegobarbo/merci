from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('pecas/', views.pecas, name='dashboard-pecas'),
    path('vendas/', views.vendas, name='dashboard-vendas')
]