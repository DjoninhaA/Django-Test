from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'Departamento: {self.nome}'



class Funcionario(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: {self.nome} | Email: {self.email} | Departamento: {self.departamento.nome}'
                                    
