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


class Anuncio(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    imovel_id = models.ForeignKey(Imovel, related_name='anuncios', on_delete=models.CASCADE)

    plataforma = models.CharField(
        null=False,
        blank=False,
        max_length=100)

    taxa_plataforma = models.FloatField()
    
    criacao = models.DateTimeField(auto_now_add=True)
    
    atualizacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['imovel_id', 'id']
        ordering = ['id']

    def __str__(self):
        return '%d: %s' % (self.id, self.plataforma)


class Reserva(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    anuncio_id = models.ForeignKey(Anuncio, related_name='reservas', on_delete=models.CASCADE)

    check_in = models.DateField(auto_now_add=False)

    check_out = models.DateField(auto_now_add=False)

    preco_total = models.FloatField()
    
    comentario = models.CharField(
        null=False,
        blank=False,
        max_length=500)

    hospedes = models.IntegerField(
        null=False,
        blank=False,
        default=0)

    criacao = models.DateTimeField(auto_now_add=True)
    
    atualizacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['anuncio_id', 'id']
        ordering = ['id']

    def __str__(self):
        return '%d: %s' % (self.id, self.preco_total)