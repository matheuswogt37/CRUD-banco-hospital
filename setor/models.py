from django.db import models

class Setor(models.Model):
    id_pk = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, blank=True, null=True)
    funcao = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setor'