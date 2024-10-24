# gestao_departamentos/urls.py
from django.urls import path
from .views import DepartamentoCreate, DepartamentoList, DepartamentoUpdate, DepartamentoDelete


urlpatterns = [
    path('create/', DepartamentoCreate.as_view(), name='departamento-list-create'),
]