from django.urls import path, include

from . import views

urlpatterns = [
    path('funcionarios/', views.funcionario_list, name='funcionario_list'),
]
