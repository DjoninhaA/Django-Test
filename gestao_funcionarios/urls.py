from django.urls import path, include

from . import views

urlpatterns = [
    path('funcionarios/', views.funcionario_list, name='funcionario_list'),
    path('funcionario/update/<int:funcionario_id>', views.funcionario_detail, name='funcionario_detail'),
    path('funcionario/delete/<int:funcionario_id>', views.funcionario_delete, name='funcionario_delete'),
]
