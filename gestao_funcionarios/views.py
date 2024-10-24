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
    

@csrf_exempt
def funcionario_detail(request, funcionario_id):
    try:
        funcionario = Funcionario.objects.get(id = funcionario_id)
    except Funcionario.DoesNotExist:
        return JsonResponse({'error': 'Funcionário não encontrado.'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({
            'id': funcionario.id,
            'nome': funcionario.nome,
            'email': funcionario.email,
            'departamento': funcionario.departamento.nome
        })
    
    elif request.method == 'PUT':
        data = json.loads(request.body)

        funcionario.nome = data.get('nome', funcionario.nome)
        funcionario.email = data.get('email', funcionario.email)

        novo_departamento_nome = data.get('departamento')
        if novo_departamento_nome:
            departamento, created = Departamento.objects.get_or_create(nome=novo_departamento_nome)
            funcionario.departamento = departamento

        try:
            funcionario.save()
            return JsonResponse({'id': funcionario.id, 'nome': funcionario.nome, 'email': funcionario.email, 'departamento': funcionario.departamento.nome}, status=200)
        except:
            return JsonResponse({'error': 'Email já cadastrado.'}, status=400)

@csrf_exempt
def funcionario_delete(request, funcionario_id):
    try:
        funcionario = Funcionario.objects.get(id = funcionario_id)
    except Funcionario.DoesNotExist:
        return JsonResponse({'error': 'Funcionário não encontrado.'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({
            'id': funcionario.id,
            'nome': funcionario.nome,
            'email': funcionario.email,
            'departamento': funcionario.departamento.nome
        })


    elif request.method == 'DELETE':
        funcionario.delete()
        return JsonResponse({'message': f'Funcionário {funcionario.nome} excluído com sucesso.'}, status=200)            