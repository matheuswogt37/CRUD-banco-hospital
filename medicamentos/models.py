from django.db import models

class Medicamentos(models.Model):
    id_pk = models.AutoField(primary_key=True)
    nome_generico = models.CharField(max_length=70, blank=True, null=True)
    nome_comercial = models.CharField(max_length=50, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    preco_unit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicamentos'