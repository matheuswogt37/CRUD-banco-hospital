from django.db import models

#* not necessary use id because will be create automatically as primary key autoincrement
class Setor(models.Model):
    nome = models.CharField(max_length=20);
    funcao = models.CharField(max_length=20);

    # def __str__(self):
    #     return f"{self.nome} - {self.funcao}"