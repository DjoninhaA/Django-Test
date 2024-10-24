from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APIClient
from .models import Departamento
from rest_framework import status

class DepartamentoTestCase(TestCase):

    def setUp(self):
        Departamento.objects.create(nome="RH")
        
        self.api_client = APIClient()

    def test_list_departamentos(self):
        url = reverse("departamento-list")
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
