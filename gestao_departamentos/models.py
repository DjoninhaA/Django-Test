from django.db import models

class Departamento(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'Departamento: {self.nome}'
