import json
from django.http import JsonResponse, HttpResponse
from .models import Funcionario

# Create your views here.

def funcionario_list(request):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all().values('nome', 'email', 'departamento')
        return JsonResponse(list(funcionarios))
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        funcionario = Funcionario(nome = data ['nome'], email = data['email'], departamento = data['departamento'])
        funcionario.save()
        return JsonResponse({'nome': funcionario.nome, 'email': funcionario.email, 'departamento': funcionario.departamento}, status = 201)
        

        ## commita como create funcionario