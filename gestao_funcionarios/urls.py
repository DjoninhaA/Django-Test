from django.urls import path, include

from gestao_funcionarios.views import funcionario_list, funcionario_detail

urlpatterns = [
    path('funcionarios/', funcionario_list, name='funcionario_list'),
    path('funcionarios/<str:nome>/', funcionario_detail, name='funcionario_detail'),
]
