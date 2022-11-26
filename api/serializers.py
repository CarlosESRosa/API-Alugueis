from rest_framework import serializers
from api.models import Imovel, Anuncio, Reserva


class ImovelSerializer(serializers.ModelSerializer):
    anuncios = serializers.StringRelatedField(many=True, required=False)
    
    class Meta:
        model = Imovel
        fields = [
            'id',
            'max_hospedes',
            'banheiros',
            'pet',
            'limpeza',
            'ativacao',
            'criacao',
            'atualizacao',
            'anuncios'
        ]


class AnuncioSerializer(serializers.ModelSerializer):
    reservas = serializers.StringRelatedField(many=True, required=False)


    class Meta:
        model = Anuncio
        fields = [
            'id',
            'imovel_id',
            'plataforma',
            'taxa_plataforma',
            'criacao',
            'atualizacao',
            'reservas'
        ]


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = [
            'id',
            'anuncio_id',
            'check_in',
            'check_out',
            'preco_total',
            'comentario',
            'hospedes',
            'criacao',
            'atualizacao',
        ]