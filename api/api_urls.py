from django.urls import include, path

from rest_framework import routers
from gestao_departamentos import views


router = routers.DefaultRouter()
router.register(r'departamento', views.DepartamentoViewSet)

urlpatterns =  [
    path('', include(router.urls))
]

