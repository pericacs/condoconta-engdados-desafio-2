from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from fintech.models import Transacao


class TransacaooSerializer(ModelSerializer):    
    class Meta:
        model = Transacao
        fields = (
           'transaction_id', 'vl_transacao', 
            'nu_conta_pagador', 'nu_conta_beneficiario', 'dt_transacao'
        )        


    def create(self, validated_data):

        transacoes = Transacao.objects.create(**validated_data)        
        transacoes.save()
        return transacoes

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nu_conta_pagador, obj.nu_conta_beneficiario)