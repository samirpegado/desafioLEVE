from django.db import models


class Add(models.Model):
    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    fone = models.CharField(max_length=11, blank=True, null=True)
    cursoadd = models.CharField(max_length=100, blank=True, null=True)



