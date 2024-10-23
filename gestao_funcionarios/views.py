import json
from venv import create
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Departamento, Funcionario
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def funcionario_list(request):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.select_related('departamento').values('nome', 'email', 'departamento__nome')
        return JsonResponse(list(funcionarios), safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)

        departamento_nome = data.get('departamento')
        departamento, created = Departamento.objects.get_or_create(nome=departamento_nome)

        funcionario = Funcionario(nome = data ['nome'], email = data['email'], departamento = departamento)
        funcionario.save()

        departamento_data = {
            'nome': departamento.nome
        }

        return JsonResponse({'nome': funcionario.nome, 'email': funcionario.email, 'departamento': departamento_data}, status = 201)
    
        
def funcionario_detail(request, nome):
    funcionario = get_object_or_404(Funcionario, nome = nome)

    if request.method == 'GET':
        return JsonResponse({'nome': funcionario.nome, 'email': funcionario.email, 'departamento': funcionario.departamento.nome})
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        funcionario.nome = data.get('nome', funcionario.nome)
        funcionario.email = data.get('email', funcionario.email)
        funcionario.departamento = data.get('departamento', funcionario.departamento.nome)
        funcionario.save()
        return JsonResponse({'nome': funcionario.nome, 'email': funcionario.email, 'departamento': funcionario.departamento})
    
    elif request.method == 'DELETE':
        funcionario.delete()
        return HttpResponse({'nome': funcionario.nome, 'email': funcionario.email, 'departamento': funcionario.departamento}, status = 204)
