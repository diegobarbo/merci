from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('pecas/', views.pecas, name='dashboard-pecas'),
    path('pecas/delete/<int:pk>/', views.peca_delete, name='dashboard-peca-delete'),
    path('pecas/update/<int:pk>/', views.peca_update, name='dashboard-peca-update'),
    path('vendas/', views.vendas, name='dashboard-vendas')
]