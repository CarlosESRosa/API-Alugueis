from django.db import models
import uuid


class Imovel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    max_hospedes = models.IntegerField(
        null=False,
        blank=False,
        default=0)

    banheiros = models.IntegerField(
        null=False,
        blank=False,
        default=0)

    pet = models.BooleanField(
        null=False,
        blank=False,
        default=False) 
    
    limpeza = models.FloatField()
    
    ativacao = models.DateTimeField(auto_now_add=True)
    
    criacao = models.DateTimeField(auto_now_add=True)
    
    atualizacao = models.DateTimeField(auto_now_add=True)