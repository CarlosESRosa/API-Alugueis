from rest_framework import serializers
from api.models import Imovel


class ImovelSerializer(serializers.ModelSerializer):
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
        ]