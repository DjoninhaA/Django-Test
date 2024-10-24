from django.urls import include, path

from rest_framework import routers
from gestao_departamentos import views as departamento_views
from gestao_funcionarios import views as funcionario_views


router = routers.DefaultRouter()
router.register(r'departamento', departamento_views.DepartamentoViewSet)
router.register(r'funcionario', funcionario_views.FuncionarioViewSet)

urlpatterns =  [
    path('', include(router.urls))
]

