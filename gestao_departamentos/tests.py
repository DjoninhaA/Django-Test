from django.test import TestCase

from .models import Departamento

class DepartamentoTestCase(TestCase):
    def setUp(self):
        Departamento.objects.create(name="RH")