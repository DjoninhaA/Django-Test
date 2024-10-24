import json
from django.http import JsonResponse

from rest_framework.viewsets import ModelViewSet
from gestao_departamentos.models import Departamento
from .serializers import DepartamentoSerializer


class DepartamentoViewSet(ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

