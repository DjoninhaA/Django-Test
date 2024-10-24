import json
from django.http import JsonResponse
from django.shortcuts import render

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from gestao_departamentos.models import Departamento


class DepartamentoList(View):
    @csrf_exempt
    def get(self, request):
        departamentos = list(Departamento.objects.values('id','nome'))
        return JsonResponse(departamentos, safe=False)
    
class DepartamentoCreate(View):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        departamento = Departamento(nome=data['nome'])
        departamento.save()
        return JsonResponse({'id': departamento.id, 'nome': departamento.nome}, status=201)
    
class DepartamentoUpdate(View):
    @csrf_exempt
    def put(self, request, id):
        data = json.loads(request.body)
        try:
            departamento = Departamento.objects.get(id=id)
            departamento.nome = data['nome']
            departamento.save()
            return JsonResponse({'id': departamento.id, 'nome': departamento.nome}, status=200)
        except Departamento.DoesNotExist:
            return JsonResponse({'error': 'Departamento não encontrado.'}, status=404)
        

class DepartamentoDelete(View):
    @csrf_exempt
    def delete(self, request, id):
        try:
            departamento = Departamento.objects.get(id=id)
            departamento.delete()
            return JsonResponse({'success': 'Departamento deletado com sucesso.'}, status=204)
        except Departamento.DoesNotExist:
            return JsonResponse({'error': 'Departamento não encontrado.'}, status=404)