# gestao_departamentos/urls.py
from django.urls import path
from .views import DepartamentoCreate, DepartamentoList, DepartamentoUpdate, DepartamentoDelete


urlpatterns = [
    path('create/', DepartamentoCreate.as_view(), name='departamento-list-create'),
    # path('getall/', DepartamentoList.as_view(), name='departamento-detail'),
    # path('update/<int:id>', DepartamentoUpdate.as_view(), name='departamento-update'),
    # path('delete/<int:id>/', DepartamentoDelete.as_view(), name='departamento-delete'), 
]
